const { app, BrowserWindow, globalShortcut, BrowserWindowConstructorOptions } = require('electron')



function createWindow () {

  /** @type {BrowserWindowConstructorOptions} */

  const opts = {

    width: 900,

    height: 560,

    alwaysOnTop: true,

    frame: true,

    transparent: false,

    webPreferences: { nodeIntegration: true, contextIsolation: false }

  }

  const win = new BrowserWindow(opts)

  win.loadFile('index.html')

}



app.whenReady().then(() => {

  createWindow()

  globalShortcut.register('F9', () => {

    const all = BrowserWindow.getAllWindows()

    if (all[0]) all[0].setAlwaysOnTop(!all[0].isAlwaysOnTop())

  })

})



app.on('will-quit', () => { globalShortcut.unregisterAll() })

