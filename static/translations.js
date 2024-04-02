// Object containing translations keyed by element id
const translationsById = {
    "pageTitle": "Seed.link",
    "headerTitle": "Seed.link - Predicción de Fertilizantes",
    "welcomeMsg": "Bienvenido al Jardín Inteligente. Este es un sistema diseñado para ayudarte a optimizar el crecimiento de tu jardín con recomendaciones inteligentes. Aprende a mejorar la fertilidad de tu jardín con nuestras herramientas de predicción avanzadas.",
    "gardeningTipsLink": "Consejos de Jardinería y Compostaje",
    "tempLabel": "Temperatura:",
    "humidLabel": "Humedad:",
    "moisLabel": "Humedad del Suelo:",
    "nitroLabel": "Nitrógeno:",
    "potaLabel": "Potasio:",
    "phosLabel": "Fósforo:",
    "soilTypeLabel": "Tipo de Suelo:",
    "predictButton": "Predecir",
    "fertilizerRecommendation": "Fertilizante Recomendado:",
    "organicAlternativesTitle": "Alternativas Orgánicas:",
    "moreInfoTitle": "Recursos para Más Información:",
    "gardeningTipsTitle": "Consejos de Jardinería y Compostaje",
    "tipsHeaderTitle": "Consejos para Principiantes de Jardinería y Compostaje",
    "tipsIntro": "Descubre los secretos para comenzar tu propio jardín y crear compost, incluso con un presupuesto ajustado.",
    "gettingStartedTitle": "Comenzando con la Jardinería",
    "gettingStartedDesc": "Iniciar un jardín puede ser una experiencia gratificante. Aquí tienes algunos consejos para comenzar, incluso en espacios limitados o con recursos limitados:",
    "startSmall": "<strong>Empieza Pequeño:</strong> Comienza con unas pocas macetas o un pequeño terreno para gestionar tu carga de trabajo y costos.",
    "useWhatYouHave": "<strong>Usa lo que Tienes:</strong> Recicla contenedores o encuentra macetas y herramientas de jardinería gratuitas en grupos comunitarios o en mercados en línea.",
    "chooseLowCostPlants": "<strong>Elige Plantas de Bajo Costo:</strong> Opta por semillas o esquejes de amigos y familiares. Algunas verduras fáciles de cultivar incluyen lechuga, rábanos y tomates.",
    "compost": "<strong>Compost:</strong> Crea tu propia tierra rica en nutrientes compostando restos de cocina y desechos de jardín.",
    "waterWisely": "<strong>Riega con Sabiduría:</strong> Recolecta agua de lluvia y aprende los mejores momentos para regar tus plantas para ahorrar en tu factura de agua.",
    "gettingStartedResources": "Para obtener una guía más detallada, consulta la <a href='https://www.gardeners.com/how-to/vegetable-gardening/5069.html' target='_blank'>Guía de Jardinería de Vegetales de Gardener's Supply Company</a> y este útil <a href='https://www.youtube.com/watch?v=IOu0DuxFAT0' target='_blank'>video sobre cómo comenzar un jardín de vegetales</a>.",
    "creatingCompostTitle": "Creando tu Propio Compost",
    "creatingCompostDesc": "¡Compostar es más fácil de lo que piensas! Aquí te mostramos cómo empezar a convertir tus desechos de cocina y jardín en oro:",
    "chooseSpot": "<strong>Elige un Lugar:</strong> Cualquier rincón de tu jardín o balcón puede albergar un pequeño contenedor de compost.",
    "balanceGreensBrowns": "<strong>Equilibra los Verdes y los Marrones:</strong> Mezcla partes iguales de materiales verdes (restos de vegetales, posos de café) y marrones (hojas secas, cartón).",
    "keepItMoist": "<strong>Manténlo Húmedo:</strong> Tu compost debe estar húmedo, pero no mojado, para apoyar la descomposición.",
    "turnRegularly": "<strong>Gira Regularmente:</strong> Airea tu compost dándole la vuelta cada pocas semanas para acelerar el proceso.",
    "creatingCompostResources": "Para métodos de compostaje económicos, explora la <a href='https://www.epa.gov/recycle/composting-home' target='_blank'>guía de compostaje en casa de la EPA</a>. Además, este <a href='https://www.youtube.com/watch?v=n9OhxKlrWwc' target='_blank'>tutorial en video sobre compostaje</a> puede proporcionar ayuda visual a los principiantes.",
    "snapBenefitsTitle": "Maximizando los Beneficios de SNAP para la Jardinería",
    "snapBenefitsDesc": "Para personas y familias que reciben beneficios de SNAP, la jardinería ofrece una oportunidad única para extender esos beneficios cultivando tu propia comida. Utilizar los beneficios de SNAP para comprar semillas y plantas puede llevar a una producción de alimentos sostenible, proporcionando productos frescos y nutritivos directamente desde tu patio trasero o jardín comunitario.",
    "snapBenefitsTips": "Aquí tienes algunos consejos para comenzar tu jardín con los beneficios de SNAP:",
    "verifyEligibleItems": "Verifica los artículos elegibles: Las semillas y plantas que producen alimentos para el consumo del hogar se pueden comprar con los beneficios de SNAP.",
    "planYourGarden": "Planifica tu jardín: Elige plantas adecuadas para tu región y considera comenzar con vegetales y hierbas fáciles de cultivar.",
    "seekOutResources": "Busca recursos: Las extensiones cooperativas locales, los jardines comunitarios y los foros en línea pueden ofrecer valiosos consejos y apoyo para los jardineros principiantes.",
    "snapBenefitsMoreInfo": "Para obtener información más detallada sobre el uso de los beneficios de SNAP para la jardinería, visita el sitio web de <a href='https://www.snapgardens.org/snap-participant/' target='_blank'>SNAP Gardens</a>. Este recurso proporciona orientación sobre cómo aprovechar al máximo tus",
    "resourcesLowIncomeTitle": "Recursos para Jardineros de Bajos Ingresos",
    "resourcesLowIncomeDesc": "La jardinería debería ser accesible para todos. Aquí hay algunos recursos específicamente dirigidos a apoyar a las personas de bajos ingresos a comenzar sus jardines:",
    "snapGardensLink": "Jardines SNAP: Información sobre el uso de los beneficios de SNAP para comprar semillas y plantas.",
    "communityGardeningLink": "Asociación de Jardinería Comunitaria Americana: Encuentra un jardín comunitario cerca de ti o aprende cómo empezar uno.",
    "seedMoneyLink": "SeedMoney: Ofrece subvenciones y oportunidades de financiación colectiva para proyectos de jardinería.",
    "apartmentGardeningTitle": "Jardinería en Espacios Pequeños y Apartamentos",
    "apartmentGardeningDesc": "¡El espacio limitado no significa que no puedas disfrutar de la jardinería! Aquí tienes consejos para crear un oasis verde en áreas de vivienda más pequeñas:",
    "verticalGardening": "<strong>Jardinería Vertical:</strong> Utiliza el espacio vertical instalando macetas colgantes, estantes o un enrejado para cultivar plantas hacia arriba en lugar de hacia afuera.",
    "containerGardening": "<strong>Jardinería en Contenedores:</strong> Las macetas y contenedores son perfectos para espacios pequeños. Elige variedades que sean adecuadas para el cultivo en macetas, como verduras enanas, hierbas y suculentas.",
    "windowSillsBalconies": "<strong>Usa Repisas de Ventanas y Balcones:</strong> Aprovecha la luz natural colocando plantas en repisas de ventanas o balcones. Incluso un pequeño jardín de hierbas puede prosperar en estos espacios.",
    "hydroponics": "<strong>Explora la Hidroponía:</strong> Los sistemas hidropónicos te permiten cultivar plantas en agua, sin tierra. Estos sistemas pueden ser muy eficientes en términos de espacio y son perfectos para la jardinería interior.",
    "selectivePlanting": "<strong>Selecciona Cuidadosamente lo que Plantas:</strong> Concéntrate en plantas que ofrezcan un alto rendimiento o que disfrutes. Las verduras de hoja verde, los tomates cherry y las fresas son geniales para la jardinería en espacios pequeños.",
    "communityGardening": "<strong>Participa en la Jardinería Comunitaria:</strong> Si el espacio es demasiado limitado en casa, busca jardines comunitarios locales donde puedas cuidar de tu propio huerto.",
    "apartmentGardeningResources": "Para más inspiración y guías sobre la jardinería en espacios pequeños, consulta esta guía completa de <a href='https://www.balconycontainergardening.com/' target='_blank'>Balcony Container Gardening</a> y el libro \"The Vegetable Gardener's Container Bible\" por Edward C. Smith.",
    "Cost": "¡Está ahorrando en promedio $ 14 al usar estas alternativas orgánicas de urea!",
};


let originalTextById = {}; // To dynamically store original text
let currentLanguage = 'en'; // Track the current language

// Function to change language on the webpage
function changeLanguageById(targetLang) {
    document.querySelectorAll("[id]").forEach(elem => {
        if (!originalTextById[elem.id]) {
            originalTextById[elem.id] = elem.innerHTML; // Store original HTML content
        }

        if (targetLang === 'es' && translationsById[elem.id]) {
            elem.innerHTML = translationsById[elem.id]; // Use innerHTML for translations that include HTML
        } else if (targetLang === 'en' && originalTextById[elem.id]) {
            elem.innerHTML = originalTextById[elem.id]; // Restore original HTML content
        }
    });

    currentLanguage = targetLang;
    document.getElementById('lang').value = targetLang; // Update hidden input field
    fetch(`/set-language/${targetLang}`).then(response => {
        if (response.ok) {
            console.log('Language updated in session');
        }
    }).catch(error => console.error('Error updating language:', error));
    updateLanguageToggleButton(targetLang);
}


function updateLanguageToggleButton(lang) {
    const button = document.getElementById('langToggleBtn');
    if (!button) return; // Exit if button doesn't exist
    button.textContent = lang === 'es' ? 'English' : 'Español';
}

// Example usage with a toggle button
document.addEventListener('DOMContentLoaded', () => {
    const langToggleButton = document.getElementById('langToggleBtn');
    if (langToggleButton) {
        langToggleButton.addEventListener('click', () => {
            const newLang = currentLanguage === 'en' ? 'es' : 'en';
            changeLanguageById(newLang);
        });
    }
});