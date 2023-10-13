// Step 4: For each favorite food in the favoriteFoods property,
// create an HTML <li> element and place its value in the <li> element

function listTemplate(item) {
  return `<li>${item}</li>`;
}

function renderList(selector, list, template) {
  const htmlArray = list.map(template);
  document.querySelector(selector).innerHTML = htmlArray.join("");
}

renderList("#favorite-foods", personalInfo.favoriteFoods, listTemplate);
