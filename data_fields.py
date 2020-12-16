class ClientFormFields:
    RegistrationDate = "data_completare"
    FirstName = "prenume"
    LastName = "nume"
    CNP = "CNP"
    PhoneNumber = "numar_telefon"
    Email = "e_mail"
    Destinations = "locatii_dorite"
    Dates = "perioade_dorite"
    StartDate = "data_start"
    EndDate = "data_sfarsit"
    NumberOfPersons = "numar_persoane"
    AvailableAmount = "suma_disponibila"
    OfferOption = "oferta"
    PaymentOption = "plata"

    fields_list = [RegistrationDate, LastName, FirstName, CNP,
                   PhoneNumber, Email, Destinations, Dates,
                   NumberOfPersons, AvailableAmount, OfferOption, PaymentOption]


class OfferFormFields:
    ID = "ID"
    Location = "Locatie"
    Dates = "Perioade"
    MinNumberOfPersons = "Grup min"
    MaxNumberOfPersons = "Grup max"
    HotelName = "Hotel"
    HotelAddress = "Adresa Hotel"
    Confort = "Confort"
    Food = "Mese incluse"
    Rooms = "Cazari disponibile"

    fields_list = [ID, Location, Dates, MinNumberOfPersons, MaxNumberOfPersons,
                   HotelName, HotelAddress, Confort, Food, Rooms]