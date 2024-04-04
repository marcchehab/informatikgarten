
/**
 * @type {import("../config/siteConfig").UserConfig}
 */
const config = {
    // title will be displayed on the top of your site
    title: "informatikgarten.ch",
    navbarTitle: {text: "🪴 informatikgarten.ch"},
    // adding a description helps with SEO
    description: "IT-Unterricht von Marc Chéhab",
    // author of site displayed on the bottom of your site
    author: "Marc Chéhab",
    // logo image
    // logo: "/icon.png",
    // url to author website
    domain: "https://informatikgarten.ch",
    // links to the pages you want to link to in the navbar
    navLinks: [{ href: "/about", name: "About" }],
    showSidebar: true,
    search: {
        provider: "algolia",
        config: {
          appId: "ZETBYYY7SW",
          apiKey: "d4861241f6ae02294bb86caf85a0dbb8",
          indexName: "informatikgarten.ch",
        },
    },
    profileIcon: '/_ig/profile.svg',
    loginIcon: '/_ig/login.svg',
  
    // this is possiblle
    // navbarTitle: {
    //   text: "Your custom title here",
    //   logo: "/images/your-logo.svg", // optional
    // },
  };
  
  export default config;
   