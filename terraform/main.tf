resource "random_string" "container_name" {
  length  = 25
  lower   = true
  upper   = false
  special = false
}

resource "azurerm_container_group" "container" {
  name                = "${var.container_group_name_prefix}-${random_string.container_name.result}"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
  ip_address_type     = "Public"
  os_type             = "Linux"
  restart_policy      = var.restart_policy

  image_registry_credential {
    server   = "containerregistryflask.azurecr.io"
    username = var.acr_username
    password = var.acr_password
  }

  container {
    name   = "${var.container_name_prefix}-${random_string.container_name.result}"
    image  = var.image
    cpu    = var.cpu_cores
    memory = var.memory_in_gb

    environment_variables = {
      "AZURE_EMAIL_CONNECTION_STRING" = var.AZURE_EMAIL_CONNECTION_STRING
    }

    ports {
      port     = var.port
      protocol = "TCP"
    }
  }
}
