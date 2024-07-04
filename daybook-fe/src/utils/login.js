const isAuthenticated = (cookieName = "session") => {
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    const [currentCookieName, cookieValue] = cookies[i].trim().split("=");

    if (currentCookieName === cookieName) {
      return true;
    }
  }

  return false;
};

export default isAuthenticated;
