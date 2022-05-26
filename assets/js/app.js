const overlay = document.querySelector('.overlay');
const hamburgerIcon = document.querySelector('.hamburger-icon');
const sidebarClose = document.querySelector('.sidebar-close');
const sidebar = document.querySelector('.sidebar');

function toggleSidebar(element, className) {
  if (element.classList.contains(className)) {
    element.classList.remove(className);
  } else {
    element.classList.add(className);
  }
}

hamburgerIcon.addEventListener('click', () => {
  toggleSidebar(sidebar, 'active');
  overlay.style.display = 'block';
});

if (sidebar) {
  sidebar.addEventListener('click', () => {
    toggleSidebar(sidebar, 'active');
    overlay.style.display = 'none';
  });
}


//message
const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 3000);
}


// document.getElementsById('actives').onclick =>(){
//   document.getElementsById('actives').style = "color: red";
// }

const activeButton = document.getElementById('actives');

// activeButton.addEventListener("click",()=>{
//   console.log("kaj koirche");
//   style = "color: red";
// })

function active(){
  console.log("kaj koreni?");
}

activeButton.addEventListener("click",active)