{
    "name": "Package Calculation",
    "version": "17.0.1.0.0",
    "summary": "This module create a calculation package",
    "category": "Inventory/Inventory",
    "author": "Treming",
    "maintainer": "Livingston Arias Narváez",
    "website": "https://github.com/Livinarias/treming",
    "license": "LGPL-3",
    "depends": [
        "stock",
        "sale_management",
        "sale_stock",
        "l10n_latam_base",
        "base_setup",
    ],
    "data": [
        # data
        "data/ir_module_category_data.xml",
        # security
        "security/package_security.xml",
        "security/ir.model.access.csv",
        # views
        "views/res_config_settings_views.xml",
        "views/package_calculation_view.xml",
        "wizard/validate_data_wizard_view.xml",
        # reports
    ],
    "installable": True,
    "auto_install": True,
    "application": True,
}
