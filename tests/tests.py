from main import mask_maestro_number, mask_visa_number, last_operations, mask_number



def test_mask_visa_number():
    assert mask_visa_number("Visa Gold 5999414228426353") == "Visa Gold 5999 4142 **** 6353"

def test_mask_maestro_number():
    assert mask_maestro_number("Maestro 3928549031574026") == "Maestro 3928 5490 **** 4026"

def test_last_operations():
    assert len(last_operations()) == 5

def test_mask_number():
    assert mask_number("Счет 84163357546688983493") == "Счет **3493"

