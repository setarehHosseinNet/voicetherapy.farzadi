  function toggleMenu() {
            const navMenu = document.getElementById('nav-menu');
            navMenu.classList.toggle('active');
        }

        // Initialize Swiper
        const swiper = new Swiper('.swiper-container', {
            loop: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
             autoplay: {
            delay: 3000, // تاخیر ۳ ثانیه بین تغییر اسلایدها
         disableOnInteraction: false, // ادامه autoplay حتی پس از تعامل کاربر
    },
        });