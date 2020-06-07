const { app, BrowserWindow } = require('electron')
const ipcMain = require('electron').ipcMain
let spawn = require('child_process').spawn;

let win ; 

function createWindow () {
  // Create the browser window.
  win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })
  //win.setMenuBarVisibility(null);
  // and load the index.html of the app.
  win.loadFile('index.html')
  //win.webContents.openDevTools()
}

function uint8arrayToString(data){
  return String.fromCharCode.apply(null, data);
};




app.on('window-all-closed', () => {
    app.quit()
})

ipcMain.on('login', (event, arg) => {
  arg = {...arg , page : "content"}
  win.webContents.send('swapPage',arg)
  
})

ipcMain.on('start', (event, arg) => {
  username  = arg.username;
  password = arg.password;
  filepath = arg.filepath;
  browser = arg.browser;
  
  
  const python = spawn("python",["./src/update.py",username,password,filepath,browser])
  python.stderr.on('data',(data)=>{
    console.log(uint8arrayToString(data))
  })
  python.stdout.on('data',(data)=>{
    console.log(uint8arrayToString(data))
  })
 
})


app.whenReady().then(createWindow)