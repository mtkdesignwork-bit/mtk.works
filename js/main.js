// ヘッダー：スクロールしたら背景とロゴを表示
(() => {
  const header = document.querySelector('.header');
  const update = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
  update();
  window.addEventListener('scroll', update, { passive: true });
})();

// ハンバーガーメニュー（スマホ）
(() => {
  const toggle = document.querySelector('.header__toggle');
  const nav = document.getElementById('global-nav');
  if (!toggle || !nav) return;

  const setOpen = (open) => {
    document.body.classList.toggle('is-menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.querySelector('.visually-hidden').textContent = open ? 'メニューを閉じる' : 'メニューを開く';
  };

  toggle.addEventListener('click', () => setOpen(!document.body.classList.contains('is-menu-open')));
  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setOpen(false);
  });
})();

// 作品画像をクリックで拡大表示
(() => {
  const dialog = document.createElement('dialog');
  dialog.className = 'lightbox';
  dialog.innerHTML = '<div class="lightbox__inner"><img alt=""></div><button class="lightbox__close" type="button" aria-label="閉じる">&times;</button>';
  document.body.appendChild(dialog);
  const img = dialog.querySelector('img');

  document.querySelectorAll('.work__img img').forEach((thumb) => {
    thumb.setAttribute('tabindex', '0');
    const open = () => {
      img.src = thumb.src;
      img.alt = thumb.alt;
      dialog.showModal();
    };
    thumb.addEventListener('click', open);
    thumb.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') open();
    });
  });

  // 画像の外側や×を押したら閉じる
  dialog.addEventListener('click', (e) => {
    if (e.target !== img) dialog.close();
  });
})();

// スクロールアニメーション：画面に入った要素に .is-visible を付ける
(() => {
  const targets = document.querySelectorAll('.js-fade');

  if (!('IntersectionObserver' in window)) {
    targets.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: '0px 0px -10% 0px', threshold: 0.05 }
  );

  targets.forEach((el) => observer.observe(el));
})();
