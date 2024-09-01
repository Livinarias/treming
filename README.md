
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/Treming/treming_tecnical_test/actions/workflows/pre-commit.yml/badge.svg?branch=17.0)](https://github.com/Treming/treming_tecnical_test/actions/workflows/pre-commit.yml?query=branch%3A17.0)
[![Build Status](https://github.com/Treming/treming_tecnical_test/actions/workflows/test.yml/badge.svg?branch=17.0)](https://github.com/Treming/treming_tecnical_test/actions/workflows/test.yml?query=branch%3A17.0)
[![codecov](https://codecov.io/gh/Treming/treming_tecnical_test/branch/17.0/graph/badge.svg)](https://codecov.io/gh/Treming/treming_tecnical_test)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# project to technical test that create a module to calculate time to recieve packing

project to create reporting to track time and price recieve packing

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

This part will be replaced when running the oca-gen-addons-table script from OCA/maintainer-tools.

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Treming
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
## User Manual

1. Clone repository.
2. Create virtualenv with Python 3.8 or newer
3. Install dependencies
4. Run docker-compose to obtain docker instance
5. Install package calculation module
6. Create package calculation records to validate funcionality
7. Click in button Done Validation for create res.partner
8. Click in button Localice to compute delivery cost ande delivery date
9. Go to Sales module to validate sale order, its has delivery date and product sellect like delivery cost.

### Aditionals
- Use template repository https://github.com/OCA/oca-addons-repo-template for quality dev.
- In model groups create packege user and andmin, for use module.
- In settings create 3 fields for api key and urls to use georeference api

---
# Sección en Español
---
## Manual de Usuario

1. Clona el repositorio
2. Crea un ambiente virtual con la versión de python 3.8 o superior.
3. Instala las dependencias.
4. Corre el archivo docker-compose para tener la instancia de odoo.
5. Instala el modulo Cálculo de Paquetes.
6. Crea un registro en el modulo.
7. Dale click al boton validar, esto creara el contacto.
8. Dale click en el boton localizar, esto calculara la fecha y costo de envio.
9. Ve al modulo de ventas, ahí encontrarás la orden con la fecha de entrega y un producto con el costo del envio, seleccionado previamente en el modelo Calculo de paquetes. 

### Adicionales

- Use el repositorio https://github.com/OCA/oca-addons-repo-template para la calidad del desarollo.
- En el modelo de grupos, cree el grupo usuario y administrador para el modulo Calculo de paquetes.
- In configuración general, cree 3 campos para colocar los datos de la api de georeferenciación (clave api, url ciudades y url zona horaria).