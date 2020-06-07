
(function(){
    
    const ipcRenderer = require('electron').ipcRenderer;
    
    let currentPage="content",previousPage = "login";
    
    let path = {
        "login" : ['./components/login/login.html',0],
        "content" : ["./components/content/content.html",0]
    }
    
    let loadPage = function(page){
        swapPages(page)
        if(path[page][1] === 0){
            var xhr= new XMLHttpRequest();
            xhr.open('GET', path[page][0], true);
            xhr.onreadystatechange= function() {
                if (this.readyState!==4) return;
                if (this.status!==200) return; // or whatever error handling you want
                document.getElementById(page).innerHTML= this.responseText;
            };
            xhr.send();
            path[page][1] = 1
        }
    }

    let swapPages = function(page){
        previousPage = currentPage
        currentPage = page
        document.getElementById(previousPage).classList.add("hide")
        document.getElementById(page).classList.remove('hide')
    }
    
    
    window.onload = function(event){
        loadPage("login")
    }

    ipcRenderer.on("swapPage",(event,arg) => {
        page = arg["page"]
        loadPage(page)
        
    })

})()
