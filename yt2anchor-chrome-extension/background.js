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
      let url = new URL(currentTabUrlString);
      let topDomain = url.hostname.split('.').splice(1).join('.');
      if (topDomain == 'youtube.com') {
        let videoId = url.searchParams.get('v');
        // let response = await fetch('https://jsonplaceholder.typicode.com/users', { method: 'GET' }); // For testing
        let response = await fetch(fetchHostName + '?id=' + videoId, { method: 'GET' });
        let responseText = await response.text();
        if (responseText.includes('Django admin')) {
          alert('You must first authenticate to use this extension');
        } else {
          alert(responseText);
        }
      } else {
        alert('This extension only works with YouTube.');
      }
    }
  );
});
