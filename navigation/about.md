---
layout: post
title: About
permalink: /about/
comments: true
---

## Places that shaped me

From the coast of San Diego to family visits across the country and the world,
these places are part of my story. This responsive grid is generated from a
JavaScript data array.

<style>
    .flag-story {
        --flag-ink: #f7f8ff;
        --flag-muted: #c7cee2;
        --flag-surface: #151c2c;
        --flag-line: rgba(199, 206, 226, 0.2);
        --flag-accent: #ffb45c;
        margin: 2rem 0 4rem;
    }

    .flag-story__intro {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 1rem;
        color: var(--flag-muted);
        font-size: 0.9rem;
    }

    .flag-story__label {
        color: var(--flag-accent);
        font-weight: 700;
    }

    .grid-container {
        gap: 1rem;
    }

    .grid-item {
        min-width: 0;
        overflow: hidden;
        border: 1px solid var(--flag-line);
        border-radius: 14px;
        background: var(--flag-surface);
        color: var(--flag-ink);
        box-shadow: 0 12px 30px rgba(2, 6, 18, 0.22);
        transition: transform 180ms ease-out, border-color 180ms ease-out;
    }

    .grid-item:hover {
        transform: translateY(-4px);
        border-color: rgba(255, 180, 92, 0.62);
    }

    .grid-item__flag-wrap {
        display: grid;
        place-items: center;
        min-height: 9.25rem;
        padding: 1.25rem;
        background: #f7f8fb;
    }

    .grid-item img {
        display: block;
        width: 100%;
        height: 7rem;
        object-fit: contain;
    }

    .grid-item__copy {
        padding: 1.15rem 1.2rem 1.3rem;
    }

    .grid-item__place,
    .grid-item__greeting,
    .grid-item__description {
        margin: 0;
    }

    .grid-item__place {
        color: var(--flag-muted);
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .grid-item__greeting {
        margin-top: 0.25rem;
        color: var(--flag-ink);
        font-size: clamp(1.35rem, 4vw, 1.75rem);
        font-weight: 750;
        line-height: 1.15;
    }

    .grid-item__description {
        margin-top: 0.65rem;
        color: var(--flag-muted);
        line-height: 1.55;
    }

    .flag-story__fallback {
        padding: 1rem;
        border: 1px solid var(--flag-line);
        border-radius: 14px;
        color: var(--flag-muted);
    }

    @media (max-width: 560px) {
        .flag-story__intro {
            align-items: flex-start;
            flex-direction: column;
        }

        .grid-item__flag-wrap {
            min-height: 8rem;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .grid-item {
            transition: none;
        }

        .grid-item:hover {
            transform: none;
        }
    }
</style>

<section class="flag-story" aria-labelledby="flag-grid-heading">
    <div class="flag-story__intro">
        <span id="flag-grid-heading" class="flag-story__label">Built with JavaScript + CSS Grid</span>
        <span>3 meaningful places · 1 connected story</span>
    </div>

    <!-- JavaScript creates #grid_container and every flag card inside this mount point. -->
    <div id="flag_grid_mount"></div>
    <noscript>
        <p class="flag-story__fallback">Enable JavaScript to view Adhvay's interactive flag grid.</p>
    </noscript>
</section>

<script>
    (() => {
        const outputElement = document.getElementById("flag_grid_mount");
        if (!outputElement) return;

        // A data array keeps the content separate from the DOM-building logic.
        const living_in_the_world = [
            {
                place: "San Diego, California",
                flag: "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_San_Diego%2C_California.svg",
                flagAlt: "City flag of San Diego, California",
                greeting: "Hello!",
                description: "I was born and raised in San Diego, and it will always be my home city."
            },
            {
                place: "Bengaluru, India",
                flag: "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_India.svg",
                flagAlt: "National flag of India",
                greeting: "Namaskāra!",
                description: "My paternal grandparents live in Bengaluru, and I have visited many times."
            },
            {
                place: "Cary, North Carolina",
                flag: "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_North_Carolina.svg",
                flagAlt: "State flag of North Carolina",
                greeting: "Hi!",
                description: "My cousins live in Cary, so my family and I visit often."
            }
        ];

        outputElement.innerHTML = "";

        // Create and style the responsive grid container with JavaScript.
        const container = document.createElement("div");
        container.id = "grid_container";
        container.className = "grid-container";
        container.style.display = "grid";
        container.style.gridTemplateColumns = "repeat(auto-fit, minmax(min(100%, 220px), 1fr))";

        for (const location of living_in_the_world) {
            const gridItem = document.createElement("article");
            gridItem.className = "grid-item";

            const flagWrap = document.createElement("div");
            flagWrap.className = "grid-item__flag-wrap";

            const image = document.createElement("img");
            image.src = location.flag;
            image.alt = location.flagAlt;
            image.loading = "lazy";
            image.decoding = "async";

            const copy = document.createElement("div");
            copy.className = "grid-item__copy";

            const place = document.createElement("p");
            place.className = "grid-item__place";
            place.textContent = location.place;

            const greeting = document.createElement("p");
            greeting.className = "grid-item__greeting";
            greeting.textContent = location.greeting;

            const description = document.createElement("p");
            description.className = "grid-item__description";
            description.textContent = location.description;

            flagWrap.appendChild(image);
            copy.append(place, greeting, description);
            gridItem.append(flagWrap, copy);
            container.appendChild(gridItem);
        }

        outputElement.appendChild(container);
    })();
</script>

### Journey through Life

Here is what I did at those places

- 🏫 Lots of Elementary Schools in Tucson, LA, Honolulu, and Glendale (CA)
- 🏫 Middle and High School in Glendale (CA), Hoover High graduated '77
- 🎓 Glendale CA Community College, UCLA Extension, LA Wilshire Computer Tech School '77 to '79
- ⛪ England, London Missionary for Church of Jesus Christ of Latter-day Saints '79 to '81
- 💼 Culver City, Glendale CA founder at Ashton-Tate, original PC's dBase 2 and 3 '82 to '87
- 🎓 Eugene Oregon Undergraduate CompSci Degree at University of Oregon (Go Ducks!) '89 to '91
- 💼 Eugene Oregon, founder and owner @ Microniche `88, Point Control CAD CAM developer '91 to '96
- 🏢 San Diego CA Qualcomm, Satellite Comm and 1st Mobile OS (BREW) '96 to '19
- 👨‍🏫 San Diego CA Teacher of Computer Science @ Del Norte High School San Diego '19 to present

### Culture, Family, and Fun

Everything for me, as for many others, revolves around family and faith.

- My mother told me that I was Danish, English. and Irish, here is my researched [family tree]({{site.baseurl}}/images/about/familytree.png)
- My family is pretty big as I have been married twice, my 1st wife passed away.  We have had 5 kids, 4 adopted by me, 1 biological.  Plus, there are three grandkids.  My name to my grandkids is Abuilito.
- The gallery of pics has some of my family, fun, culture and faith memories.

<comment>
Gallery of Pics, scroll to the right for more ...
</comment>
<div class="image-gallery">
  <img src="{{site.baseurl}}/images/about/missionary.jpg" alt="Image 1">
  <img src="{{site.baseurl}}/images/about/john_tamara.jpg" alt="Image 2">
  <img src="{{site.baseurl}}/images/about/tamara_fam.jpg" alt="Image 3">
  <img src="{{site.baseurl}}/images/about/surf.jpg" alt="Image 4">
  <img src="{{site.baseurl}}/images/about/john_lora.jpg" alt="Image 5">
  <img src="{{site.baseurl}}/images/about/lora_fam.jpg" alt="Image 6">
  <img src="{{site.baseurl}}/images/about/lora_fam2.jpg" alt="Image 7">
  <img src="{{site.baseurl}}/images/about/pj_party.jpg" alt="Image 8">
  <img src="{{site.baseurl}}/images/about/trent_family.png" alt="Image 9">
  <img src="{{site.baseurl}}/images/about/claire.jpg" alt="Image 10">
  <img src="{{site.baseurl}}/images/about/grandkids.jpg" alt="Image 11">
  <img src="{{site.baseurl}}/images/about/farm.jpg" alt="Image 12">
</div>
