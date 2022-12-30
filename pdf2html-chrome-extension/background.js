const fetchHostName = 'https://youtube-to-snipd.pandibay.com';

function getCurrentTabUrl() {
  return window.location.href;
}

chrome.browserAction.onClicked.addListener(async () => {
  // chrome.tabs.executeScript is necessary to be able to access DOM element,
  // in this case, the URL string of the current open tab
  await chrome.tabs.executeScript(
    {
      code: '(' + getCurrentTabUrl + ')();',
    },
    async (results) => {
      const currentTabUrlString = results[0];
      let response = await fetch(fetchHostName + '/to_html/?url=' + currentTabUrlString, { method: 'GET' });
      let responseText = await response.text();
      if (responseText.includes('Done')) {
        let filename = currentTabUrlString.split('/').slice(-1)[0];
        let dirname = filename.split('.')[0];
        // alert(dirname);
        await chrome.tabs.create({
          url: fetchHostName + '/static/pdf_to_html/' + dirname + '/index.html',
          active: true,
        });
      } else {
        alert(responseText);
      }
    }
  );
});
