Vagrant.configure("2") do |config|

  config.vm.define "selenium-example" do |se|
    se.vm.box = "centos/7"
    se.vm.hostname = "selenium-example"
  end

  config.vm.network "forwarded_port", guest: 80, host: 9080
  config.vm.network "forwarded_port", guest: 5000, host: 9050
  config.vm.synced_folder ".", "/vagrant", type:"virtualbox"
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provisioning/site.yml"
    ansible.verbose = '-vv'
    ansible.groups =  {
      "webservers" => ["selenium-example"],
      "development" => ["selenium-example"],
      "appservers" =>["selenium-example"],
    }
    # ansible.install_mode = "pip"
  end

end
