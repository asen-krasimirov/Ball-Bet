
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
let group = urlParams.get('group').toLowerCase();
let selector = '.group-' + group;

const listElement = document.querySelector(selector);

listElement.className += ' selected';
