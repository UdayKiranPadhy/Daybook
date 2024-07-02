/**
 * Removes a cookie by name.
 * @param {string} name - The name of the cookie to remove.
 */
function removeCookie(name) {
  // Set the cookie with an expiration date in the past to remove it
  document.cookie = name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
}

export { removeCookie };
