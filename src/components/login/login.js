const { dialog } = require('electron').remote
let ipcRender = require('electron').ipcRenderer

let filePath,username,password,browser;



function getUserNameAndPassword(){
    let userName = document.getElementById("username").value;
    let passWord = document.getElementById("password").value;
    let _browser = document.getElementById("browser").value;
    
    if (userName && passWord && filePath){
        removeError()
        username = userName;
        password = passWord;
        browser = _browser
        startUpload();
    }
    else {
        addError()
    }
}


function addError(){
    document.getElementById("username").style.borderColor = "red"    
    document.getElementById("password").style.borderColor = "red"
    
    if(!filePath){
        document.getElementById("message").innerHTML = "Please Upload File"
    }
}

function removeError(){
    document.getElementById("username").style.borderColor =  "#D1D1D1";
    document.getElementById("password").style.borderColor =  "#D1D1D1";
    document.getElementById("message").innerHTML = ""
}

function openFile() { 
    dialog.showOpenDialog({
        properties: ['openFile'],
        filters: [
            { name: "CSV", extensions: ["csv", "xlsx"] }
        ]
    }).then((result)=>{
        if(result){
            filePath = result.filePaths.pop()
        }   
    })
}

function uint8arrayToString(data){
    return String.fromCharCode.apply(null, data);
};

function startUpload() {
    ipcRender.send("start",{
        username : username,
        password : password,
        filepath : filePath,
        browser : browser
    })
}