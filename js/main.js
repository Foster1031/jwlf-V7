/* ============================================================
   JWLF — sitewide vanilla JavaScript (no dependencies)
   1. Mobile navigation + dropdown/accordion sub-menus
   2. Photo-gallery lightbox
   3. Client-side form validation + demo confirmation
      (see the FORMSPREE comment inside handleForms() to go live)
   4. Gentle scroll-reveal (skipped for prefers-reduced-motion)
   ============================================================ */
(function () {
  "use strict";

  /* ---------- 1. Navigation ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Dropdowns (desktop) / accordions (mobile) — same markup, same behavior.
  document.querySelectorAll(".has-submenu > .submenu-toggle").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var li = btn.parentElement;
      var isOpen = li.classList.contains("open");
      closeAllSubmenus();
      if (!isOpen) {
        li.classList.add("open");
        btn.setAttribute("aria-expanded", "true");
        li.querySelector(".submenu").style.display = "block";
      }
    });
  });

  function closeAllSubmenus() {
    document.querySelectorAll(".has-submenu.open").forEach(function (li) {
      li.classList.remove("open");
      var b = li.querySelector(".submenu-toggle");
      if (b) b.setAttribute("aria-expanded", "false");
      var s = li.querySelector(".submenu");
      if (s) s.style.display = "";
    });
  }


  // Desktop hover support is provided in CSS (:hover / :focus-within).
  // Close any click-opened submenu after a submenu link is chosen so the
  // menu doesn't stay pinned open when navigating back.
  document.querySelectorAll(".submenu a").forEach(function (a) {
    a.addEventListener("click", function () { closeAllSubmenus(); });
  });

  // Close menus on outside click or Escape (keyboard accessible).
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-submenu")) closeAllSubmenus();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeAllSubmenus();
      if (nav && nav.classList.contains("open")) {
        nav.classList.remove("open");
        if (toggle) { toggle.setAttribute("aria-expanded", "false"); toggle.focus(); }
      }
      closeLightbox();
    }
  });

  /* ---------- 2. Lightbox (gallery pages) ---------- */
  var lightbox = document.getElementById("lightbox");
  var lbImg, lbCaption, galleryLinks = [], currentIndex = -1;

  if (lightbox) {
    lbImg = lightbox.querySelector("img");
    lbCaption = lightbox.querySelector(".lightbox-caption");
    galleryLinks = Array.prototype.slice.call(document.querySelectorAll(".gallery-grid a"));

    galleryLinks.forEach(function (link, i) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        openLightbox(i);
      });
    });

    lightbox.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
    lightbox.querySelector(".lightbox-prev").addEventListener("click", function () { step(-1); });
    lightbox.querySelector(".lightbox-next").addEventListener("click", function () { step(1); });
    lightbox.addEventListener("click", function (e) { if (e.target === lightbox) closeLightbox(); });
    document.addEventListener("keydown", function (e) {
      if (!lightbox.classList.contains("open")) return;
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });
  }

  function openLightbox(i) {
    currentIndex = i;
    var link = galleryLinks[i];
    lbImg.src = link.getAttribute("href");
    lbImg.alt = link.querySelector("img") ? link.querySelector("img").alt : "";
    lbCaption.textContent = lbImg.alt;
    lightbox.classList.add("open");
    lightbox.querySelector(".lightbox-close").focus();
    document.body.style.overflow = "hidden";
  }
  function closeLightbox() {
    if (!lightbox || !lightbox.classList.contains("open")) return;
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
    if (currentIndex > -1 && galleryLinks[currentIndex]) galleryLinks[currentIndex].focus();
  }
  function step(dir) {
    if (!galleryLinks.length) return;
    currentIndex = (currentIndex + dir + galleryLinks.length) % galleryLinks.length;
    var link = galleryLinks[currentIndex];
    lbImg.src = link.getAttribute("href");
    lbImg.alt = link.querySelector("img") ? link.querySelector("img").alt : "";
    lbCaption.textContent = lbImg.alt;
  }

  /* ---------- 3. Forms ---------- */
  /*
   * GOING LIVE WITH FORMSPREE (no backend needed):
   *   1. Create a free form at https://formspree.io (one per form is fine).
   *   2. Copy the endpoint, e.g. https://formspree.io/f/abcdwxyz
   *   3. On the <form> tag, set:  action="https://formspree.io/f/abcdwxyz"  method="POST"
   *   4. Delete (or comment out) the e.preventDefault() line below so the
   *      browser submits normally, OR keep this handler and replace the
   *      demo-confirmation block with:
   *         fetch(form.action, { method: "POST", body: new FormData(form),
   *                              headers: { Accept: "application/json" } })
   *           .then(function () { showSuccess(form); form.reset(); });
   *   Formspree will email submissions to the address you configure.
   */
  document.querySelectorAll("form[data-validate]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // DEMO MODE — remove when wiring to Formspree (see note above)
      var valid = true;

      form.querySelectorAll("[required]").forEach(function (field) {
        var row = field.closest(".form-row");
        var ok = field.value.trim() !== "";
        if (ok && field.type === "email") {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value.trim());
        }
        if (row) row.classList.toggle("invalid", !ok);
        if (!ok) valid = false;
      });

      if (!valid) {
        var firstInvalid = form.querySelector(".form-row.invalid input, .form-row.invalid select, .form-row.invalid textarea");
        if (firstInvalid) firstInvalid.focus();
        return;
      }
      showSuccess(form);
      form.reset();
    });

    // Clear an error as soon as the person fixes the field.
    form.querySelectorAll("input, select, textarea").forEach(function (field) {
      field.addEventListener("input", function () {
        var row = field.closest(".form-row");
        if (row) row.classList.remove("invalid");
      });
    });
  });

  function showSuccess(form) {
    var msg = form.parentElement.querySelector(".form-success");
    if (msg) {
      msg.classList.add("show");
      msg.setAttribute("tabindex", "-1");
      msg.focus();
    }
  }

  // Contact page: pre-fill the subject from ?subject=... (used by the
  // "Submit a forum idea" and "Speak at our events" calls-to-action).
  var subjectField = document.getElementById("contact-subject");
  if (subjectField) {
    var params = new URLSearchParams(window.location.search);
    var s = params.get("subject");
    if (s === "forum-idea") subjectField.value = "Forum idea";
    if (s === "speaking") subjectField.value = "Speaking at JWLF educational events";
    if (s === "partner") subjectField.value = "Becoming a non-profit partner";
  }

  /* ---------- 4. Scroll reveal ---------- */
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll("[data-reveal]");
  if (!reduceMotion && "IntersectionObserver" in window && revealEls.length) {
    revealEls.forEach(function (el) { el.classList.add("reveal"); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Footer year ---------- */
  var yearEl = document.getElementById("footer-year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
