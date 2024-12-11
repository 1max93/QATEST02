import pytest
from pages.form_page import FormPage
from pages.confirmation_modal_page import ConfirmationModalPage

def test_successful_registration(driver):
    form = FormPage(driver)
    form.open()

    # Remplir tous les champs obligatoires
    form.fill_name("John", "Doe")
    form.fill_email("john.doe@example.com")
    form.select_gender("Male")
    form.fill_phone("9876543210")

    # Sélection d'une date de naissance (par exemple 10 May 1990)
    form.select_date_of_birth(10, "May", 1990)

    # Ajouter une matière (par exemple "Maths")
    form.add_subject("Maths")

    # Sélectionner un loisir (ex: Sports)
    form.select_hobbies(["Sports"])

    # Ajouter une adresse
    form.fill_address("123 Test Street")

    # Sélectionner un État et une Ville (par exemple State: NCR, City: Delhi)
    form.select_state("NCR")
    form.select_city("Delhi")

    # Soumettre le formulaire
    form.submit_form()

    # Vérifier l'affichage de la modal de confirmation
    modal = ConfirmationModalPage(driver)
    confirmation_text = modal.get_confirmation_text()
    assert "Thanks for submitting the form" in confirmation_text

def test_incomplete_registration(driver):
    form = FormPage(driver)
    form.open()
    form.fill_name("Jane", "Doe")
    # Ici on ne remplit pas l'email ni le reste, la modal ne devrait pas apparaître
    form.submit_form()

    # On s'attend à une exception si on tente de récupérer la modal inexistante
    with pytest.raises(Exception):
        modal = ConfirmationModalPage(driver)
        modal.get_confirmation_text()
