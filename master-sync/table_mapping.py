TABLE_MAPPING = {
    "IMC": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code IN ('IMCC', 'IMCDI', 'IMK', 'IMM', 'RC', 'SYSK')"
    },
    "IMCB": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "Sysmac_INFO": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "DQ": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    }
}
