const title = document.querySelector('input[name=title]');
const slug = document.querySelector('input[name=slug]');

document.getElementById("id_slug").readOnly = true; // make the slug field readonly


const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-') // replaces & with -and-
    .replace(/[\s\W-]+/g,'-') // replaces space, non words chars, dashes with single dash
}

title.addEventListener('keyup', (e)=> { // event listener for input into field
    slug.setAttribute('value', slugify(title.value));
});