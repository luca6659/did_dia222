// access/fill.js

// Флаги включения дополнительных документов
var isWorking = true;
var isRightsEnabled = true;        // true - показать права, false - скрыть
var isCovidCertificateEnabled = true; // true - показать COVID-сертификат

// Данные пользователя
var fullname = "Бабаков Лука Сергійович";
var name = "Лука";
var birthdate = "05.09.2011";
var passport_id = "520471839";
var kpp_id = "05098251420";

// Данные водительского удостоверения (если isRightsEnabled = true)
var rights_valid_until = "05.09.2031";     // 20 лет с даты рождения
var rights_categories = "A, B";
var rights_tsc = "ТСЦ 8631";
var rights_id = "KBE968639";

// Данные COVID-сертификата (если isCovidCertificateEnabled = true)
var covid_valid_until = "05.09.2026";      // 5 лет с даты рождения
var covid_certificate_id = "URN:UVCI:01:UA:0E556693768";

// Подстановка данных в DOM
if(isWorking) {
    // Дата рождения
    for(el of document.getElementsByClassName("birthdate")){
        el.innerHTML = "Дата народження: " + birthdate;
    }
    
    // Полное имя
    for(el of document.getElementsByClassName("fullname")){
        el.innerHTML = fullname;
    }
    
    // Приветствие в меню
    document.getElementsByClassName("menutitile")[0].innerHTML = "Вітаємо, " + name;
    
    // Номер паспорта
    document.getElementsByClassName("passport_id")[0].innerHTML = "Номер: " + passport_id;
    
    // Номер налоговой карты (РНОКПП)
    document.getElementsByClassName("kpp_id")[0].innerHTML = kpp_id;
    
    // Данные водительского удостоверения
    if(isRightsEnabled) {
        document.getElementsByClassName("rights_valid_until")[0].innerHTML = "Дійсне до: " + rights_valid_until;
        document.getElementsByClassName("rights_categories")[0].innerHTML = "Категорії: " + rights_categories;
        document.getElementsByClassName("rights_tsc")[0].innerHTML = "Видав: " + rights_tsc;
        document.getElementsByClassName("rights_id")[0].innerHTML = rights_id;
    }
    
    // Данные COVID-сертификата
    if(isCovidCertificateEnabled) {
        document.getElementsByClassName("covid_valid_until")[0].innerHTML = "Дійсний до: " + covid_valid_until;
        document.getElementsByClassName("covid_certificate_id")[0].innerHTML = covid_certificate_id;
    }
}