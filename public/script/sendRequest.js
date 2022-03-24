//leave this empty, if backend is running on the same host as the frontend
const API_ADDRESS = ""; //eg. http://localhost:3000

/**
 * function that send GET Request to the backend
 */
const sendRequest = async ({ value: endpoint }) => {
  //build the url
  let request_url = `${API_ADDRESS}/${endpoint}`;

  //replace all double slashes with a single slash, except the one from http://
  request_url = request_url.replaceAll("//", "/");
  request_url = request_url.replaceAll(":/", "://");

  //send the request
  fetch(request_url);
};
