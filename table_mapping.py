TABLE_MAPPING = {
    "IMC-1": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code IN ('IMCC', 'IMCDI', 'IMK', 'IMM', 'RC', 'SYSK')"
    },
    "IMC-2": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "Sysmac Info System": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "SYSMAC": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    }
}
