#!powershell

#Requires -Module Ansible.ModuleUtils.Legacy

#AnsibleRequires -Become

$params = Parse-Args $args

$result = @{
    changed = $false
}

try
{
    $hv = Get-VMHost
    $result.add("computer_name",$hv.ComputerName)
    $result.add("domain_name",$hv.FullyQualifiedDomainName)
    $result.add("logical_processor_count",$hv.LogicalProcessorCount)
    $result.add("memory_capacity",$hv.MemoryCapacity)
    $result.add("iov_support",$hv.IovSupport)
    $result.add("supported_vm_versions",$hv.SupportedVMVersions)
    $result.add("virtual_machine_path",$hv.VirtualMachinePath)
    $result.add("virtual_hard_disk_path",$hv.VirtualHardDiskPath)
    $result.add("vm_migration_enabled",$hv.VirtualMachineMigrationEnabled)
    $result.add("max_vm_migrations",$hv.MaximumVirtualMachineMigrations)
    $result.add("max_storage_migrations",$hv.MaximumStorageMigrations)

    $network = @{
        internal_adapters = $hv.InternalNetworkAdapters.Name
        external_adapters = $hv.ExternalNetworkAdapters.Name
    }
    $result.add("network",$network)
}
catch
{
    $errormsg = $_.Exception.Message
    Fail-Json $result "Get-VMHost failed: $errormsg"
}

# Process changes
if($params.virtual_machine_path -and ($params.virtual_machine_path -ne $hv.VirtualMachinePath))
{
    try
    {
        Set-VMHost -VirtualMachinePath $params.virtual_machine_path
        $result.virtual_machine_path = $params.virtual_machine_path
        $result.changed = $true
    }
    catch
    {
        $errormsg = $_.Exception.Message
        Fail-Json $result "Failed to set VirtualMachinePath: $errormsg"
    }
}




Exit-Json $result
