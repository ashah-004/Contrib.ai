resource "google_compute_network" "agent_vpc"{
    name = "agent-network"
    auto_create_subnetworks = true
}

resource "google_compute_firewall" "allow_ssh" {
  name = "allow-ssh"
  network = google_compute_network.agent_vpc.name

  allow {
    protocol = "tcp"
    ports = [ "22" ]
  }

  source_ranges = [ "0.0.0.0/0" ]
}
