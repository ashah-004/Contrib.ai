resource "google_compute_instance" "agent_vm" {
  name = "contrib-agent-vm"
  machine_type = "e2-medium"
  zone = "us-west2-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size = 30
    }
  }

  network_interface {
    network = google_compute_network.agent_vpc.name
    access_config {
      
    }
  }
  
  metadata = {
    ssh-keys = "akshatshah:${file("~/.ssh/id_ed25519.pub")}"
  }
}

output "agent_vm_ip" {
  value = google_compute_instance.agent_vm.network_interface.0.access_config.0.nat_ip
  description = "The public IP address of our Agent VM"
}