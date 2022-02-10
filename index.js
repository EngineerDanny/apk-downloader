var st = document.getElementById("st");
st.addEventListener("click", scrollToTop);
function scrollToTop() {
  0 != document.body.scrollTop || 0 != document.documentElement.scrollTop
    ? (window.scrollBy(0, -50), (timeOut = setTimeout("scrollToTop()", 10)))
    : clearTimeout(timeOut);
}
window.addEventListener(
  "scroll",
  function () {
    document.body.scrollTop > 50 || document.documentElement.scrollTop > 50
      ? (st.style.display = "block")
      : (st.style.display = "none");
  },
  150
);
function preloadImage(e) {
  var ua = navigator.userAgent.toLowerCase();
  if (ua.indexOf("iphone") == -1) {
    e.src = e.dataset.src;
  } else {
    e.src = e.dataset.src.replace(/-rw$/, "");
  }
}
window.addEventListener("load", function () {
  for (
    var $searchInputs = document.querySelectorAll("input[name=q]"),
      onSearchInputClick = function (e) {
        lazy_js("/js/suggest.js");
        for (var n = 0; n < $searchInputs.length; n++)
          $searchInputs[n].removeEventListener("focus", onSearchInputClick);
      },
      k = 0;
    k < $searchInputs.length;
    k++
  )
    $searchInputs[k].addEventListener("focus", onSearchInputClick);
  if (page == "home" || page == "search") {
    document.getElementsByClassName("sbtn")[0].onclick = function () {
      window.location.href = "/search/" + $searchInputs[0].value;
    };
  } else {
    document.getElementById("nav-btn").onclick = function () {
      window.location.href = "/search/" + $searchInputs[0].value;
    };
  }

  document.getElementById("q").addEventListener("keyup", function (event) {
    if (event.keyCode === 13) {
      window.location.href = "/search/" + $searchInputs[0].value;
    }
  });
});
(function () {
  var data = new FormData();
  data.append(
    "token",
    "Z1NjU091TVdGdkVZZWNXeStDaGgvL1RXbVBKeUo1OVk2Ti9ySCtyY2JvVjA1SlF0Nzd5VlpHcGc4aGhrU05KKzBYc0VkUzZsZE5XSGNoaU5JUlpQYnVCRU5NY29qUGxKbDkvbkZJZHFDQ2pqdndtVDJVaFdqUGtocXBuQmtabWsxd1JhaVYxZlZiM0o0UEFVZVdGbkc2QURJMVdkWXEzbXdFeG9ObTJqM01zdWt2RnRlNUVIb1B6Uk9KNll6eHkzSU55UGc5eWRiZktHSFppVng0MFJpZz09"
  );
  fetch("/dl/", {
    method: "post",
    body: data,
  })
    .then((response) => response.text())
    .then((data) => {
      json = JSON.parse(data);
      if (!json.status) {
        if ((json.status_code = 429)) {
          lazy_js("https://www.google.com/recaptcha/api.js");
          document.getElementById("note").style.display = "none";
          document.getElementById("captcha").innerHTML =
            '<form action="/dl/" method="POST"><input type="hidden" name="token" value="Z1NjU091TVdGdkVZZWNXeStDaGgvL1RXbVBKeUo1OVk2Ti9ySCtyY2JvVjA1SlF0Nzd5VlpHcGc4aGhrU05KKzBYc0VkUzZsZE5XSGNoaU5JUlpQYnVCRU5NY29qUGxKbDkvbkZJZHFDQ2pqdndtVDJVaFdqUGtocXBuQmtabWsxd1JhaVYxZlZiM0o0UEFVZVdGbkc2QURJMVdkWXEzbXdFeG9ObTJqM01zdWt2RnRlNUVIb1B6Uk9KNll6eHkzSU55UGc5eWRiZktHSFppVng0MFJpZz09"><div class="g-recaptcha" data-sitekey="6LdgoSUTAAAAABSCUu7UffVQNDK0MzvA5qa_kk_n"></div><br><input type="submit" value="Submit" class="mb20 btn1 captcha-btn"></form>';
        } else if ((json.status_code = 404)) {
          document.getElementById("note").innerHTML = "404 - Find not found";
        } else {
          document.getElementById("note").innerHTML = "Something went wrong.";
        }
      } else {
        document.getElementsByClassName("box-link")[0].classList.add("show");
        document
          .getElementById("download_link")
          .setAttribute("href", json.download_link);
        document.getElementById("note").innerHTML = "Downloading...";
        // window.location.href=json.download_link
        var iframe = document.createElement("iframe");
        iframe.style.display = "none";
        iframe.src = json.download_link;
        document.body.appendChild(iframe);
      }
    });
  const config = { rootMargin: "0px", threshold: 0.05 };
  let observer = new IntersectionObserver(function (e, r) {
    e.forEach((e) => {
      e.isIntersecting && (preloadImage(e.target), r.unobserve(e.target));
    });
  }, config);
  const imgs = document.querySelectorAll("[data-src]");
  imgs.forEach((e) => {
    observer.observe(e);
  });
  var lazyLoad = false;
  function lazy_load() {
    if (lazyLoad === false) {
      lazyLoad = true;
      document.removeEventListener("scroll", lazy_load);
      lazy_js(
        "//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-61efca32e07501be"
      );
      lazy_js("https://www.googletagmanager.com/gtag/js?id=UA-40303894-22");
      lazy_js("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js");
      document.removeEventListener("mousemove", lazy_load);
      document.removeEventListener("mousedown", lazy_load);
      document.removeEventListener("touchstart", lazy_load);
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "UA-40303894-22");
    }
  }
  document.addEventListener("scroll", lazy_load),
    document.addEventListener("mousemove", lazy_load),
    document.addEventListener("mousedown", lazy_load),
    document.addEventListener("touchstart", lazy_load),
    document.addEventListener("load", function () {
      (document.body.clientHeight != document.documentElement.clientHeight &&
        0 == document.documentElement.scrollTop &&
        0 == document.body.scrollTop) ||
        lazy_load();
    });
  var a2a_loaded = false;
  document.querySelector(".sharebtn").addEventListener("click", function () {
    a2a_loaded
      ? window.a2a && window.a2a.show_full()
      : lazy_js("//static.addtoany.com/menu/page.js", function () {
          a2a.fill_menus("page");
          a2a.show_full();
        });
    a2a_loaded = true;
  });
})();
