
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
let group = urlParams.get('group');
if (!group) group = 'A';
let selector = '.group-' + group.toLowerCase();

const listElement = document.querySelector(selector);

listElement.className += ' selected';
