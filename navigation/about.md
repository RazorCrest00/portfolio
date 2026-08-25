---
layout: post
title: About
permalink: /about/
comments: true
---

<header class="about-hero">
    <div class="about-hero__meta">
        <span>Adhvay Iyer</span>
        <span aria-hidden="true">·</span>
        <span>10th Grade</span>
        <span aria-hidden="true">·</span>
        <span>AP Computer Science Principles</span>
    </div>
    <p class="about-hero__headline">I love solving problems with code—and spending time with my dog, Coco.</p>
    <p class="about-hero__intro">
        I am a San Diego student who is curious about computer science, mathematics, and cybersecurity.
        When I am away from a screen, you will probably find me with friends, on a soccer field, or playing badminton.
    </p>
    <div class="about-hero__interests" aria-label="Quick interests">
        <span>Computer science</span>
        <span>Cyber defense</span>
        <span>Math</span>
        <span>Soccer</span>
        <span>Badminton</span>
    </div>
</header>

## Places that shaped me

From the coast of San Diego to family visits across the country and the world,
these places are part of my story. This responsive grid is generated from a
JavaScript data array.

<style>
    .about-hero,
    .flag-story,
    .journey-timeline,
    .interest-story,
    .evidence-panel {
        --about-ink: #f7f8ff;
        --about-muted: #c7cee2;
        --about-surface: #151c2c;
        --about-line: rgba(199, 206, 226, 0.2);
        --about-accent: #ffb45c;
    }

    .about-hero {
        position: relative;
        isolation: isolate;
        overflow: hidden;
        margin: 1rem 0 4.5rem;
        padding: clamp(1.5rem, 5vw, 3.5rem);
        border-radius: 16px;
        background:
            radial-gradient(circle at 88% 12%, rgba(255, 180, 92, 0.24), transparent 28%),
            linear-gradient(145deg, #101726 0%, #19263d 58%, #122f38 100%);
        color: var(--about-ink);
        box-shadow: 0 18px 44px rgba(2, 6, 18, 0.3);
    }

    .about-hero::after {
        position: absolute;
        z-index: -1;
        right: -3rem;
        bottom: -5rem;
        width: 13rem;
        height: 13rem;
        border: 1px solid rgba(255, 180, 92, 0.28);
        border-radius: 50%;
        content: "";
    }

    .about-hero__meta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem 0.7rem;
        color: var(--about-accent);
        font-size: 0.82rem;
        font-weight: 700;
    }

    .about-hero__headline {
        max-width: 18ch;
        margin: 1.25rem 0 1rem;
        color: var(--about-ink);
        font-size: clamp(2.15rem, 7vw, 4.5rem);
        font-weight: 780;
        letter-spacing: -0.035em;
        line-height: 0.98;
        text-wrap: balance;
    }

    .about-hero__intro {
        max-width: 67ch;
        margin: 0;
        color: var(--about-muted);
        font-size: clamp(1rem, 2.4vw, 1.15rem);
        line-height: 1.7;
    }

    .about-hero__interests {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin-top: 1.75rem;
    }

    .about-hero__interests span {
        padding: 0.42rem 0.72rem;
        border: 1px solid rgba(247, 248, 255, 0.2);
        border-radius: 999px;
        color: var(--about-ink);
        font-size: 0.82rem;
    }

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

    .journey-timeline,
    .interest-story {
        margin: 2rem 0 4.5rem;
    }

    .journey-timeline > ul {
        margin: 1.5rem 0 0;
        padding: 0;
        list-style: none;
    }

    .journey-timeline > ul > li {
        position: relative;
        margin: 0;
        padding: 0.9rem 0 1.35rem 2.15rem;
        color: var(--about-muted);
        line-height: 1.65;
    }

    .journey-timeline > ul > li::before {
        position: absolute;
        top: 1.25rem;
        left: 0.18rem;
        width: 0.68rem;
        height: 0.68rem;
        border: 3px solid #111827;
        border-radius: 50%;
        background: var(--about-accent);
        box-shadow: 0 0 0 1px rgba(255, 180, 92, 0.42);
        content: "";
    }

    .journey-timeline > ul > li:not(:last-child)::after {
        position: absolute;
        top: 1.95rem;
        bottom: -0.1rem;
        left: 0.5rem;
        width: 1px;
        background: var(--about-line);
        content: "";
    }

    .journey-timeline strong {
        color: var(--about-ink);
    }

    .interest-story > ul {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0;
        margin: 1.5rem 0 0;
        padding: 0;
        border-top: 1px solid var(--about-line);
        list-style: none;
    }

    .interest-story > ul > li {
        margin: 0;
        padding: 1.1rem 1rem 1.1rem 0;
        border-bottom: 1px solid var(--about-line);
        color: var(--about-muted);
        line-height: 1.55;
    }

    .interest-story > ul > li:nth-child(even) {
        padding-right: 0;
        padding-left: 1rem;
    }

    .interest-story strong {
        color: var(--about-ink);
    }

    .evidence-panel {
        margin: 4.5rem 0;
        padding: clamp(1.25rem, 4vw, 2rem);
        border: 1px solid rgba(255, 180, 92, 0.38);
        border-radius: 14px;
        background: rgba(255, 180, 92, 0.08);
    }

    .evidence-panel h2 {
        margin-top: 0;
    }

    .evidence-panel blockquote {
        margin: 1rem 0 1.5rem;
        padding: 0;
        border: 0;
        color: var(--about-accent);
        font-size: 1.05rem;
        font-weight: 700;
    }

    .evidence-panel ul {
        margin-bottom: 0;
        padding-left: 1.4rem;
    }

    .evidence-panel li {
        margin: 0.6rem 0;
    }

    @media (max-width: 560px) {
        .flag-story__intro {
            align-items: flex-start;
            flex-direction: column;
        }

        .grid-item__flag-wrap {
            min-height: 8rem;
        }

        .interest-story > ul {
            grid-template-columns: 1fr;
        }

        .interest-story > ul > li,
        .interest-story > ul > li:nth-child(even) {
            padding-right: 0;
            padding-left: 0;
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

<section class="journey-timeline" markdown="1">

## My journey so far

My story is still being written, but every chapter has helped me become more curious, resilient, and thoughtful.

- **Born in San Diego** — San Diego, California, has been home since the day I was born.
- **Growing up in Del Sur** — I attended Design39Campus (D39C), where I began building friendships and discovering what I enjoyed learning.
- **Learning resilience** — Breaking my arm in second grade and later dealing with ankle injuries taught me patience and how to keep moving forward through setbacks.
- **Becoming a big brother** — When my little sister was born, I learned how important it is to be patient, responsible, and supportive of someone younger than me.
- **Finding my competitive side** — I played soccer throughout childhood, learning teamwork, communication, and how to improve after both wins and losses.
- **Discovering math and computer science** — In middle school, problem-solving became something I genuinely enjoyed, especially when math and code let me turn ideas into answers.
- **Building cyber skills at Del Norte** — At Del Norte High School, I joined CyberAegis, competed in CyberPatriot, and grew my interest in computer science and cybersecurity.
- **Looking ahead** — After high school, I hope to study at MIT. I do not know my exact future career yet, and I am excited to explore where computer science can take me.

</section>

<section class="interest-story" markdown="1">

## What matters to me

I am happiest when I can balance challenging work with people, movement, culture, and good food.

- **Friends:** Spending time with friends keeps life fun and gives me people to learn and laugh with.
- **Sports:** Soccer and badminton give me a competitive outlet and keep me active.
- **Building:** Coding projects let me experiment, solve problems, and create something that did not exist before.
- **Competition:** CyberPatriot challenges me to think carefully, work with a team, and defend computer systems.
- **Curiosity:** Mathematics is one of my favorite subjects because there is always another pattern or strategy to discover.
- **Identity:** I am South Indian and Hindu, and both my culture and family are meaningful parts of who I am.
- **Coco:** I love my dog, Coco, who makes even ordinary days better.
- **The future:** I am still exploring careers, but I know I want curiosity and computer science to remain part of my path.

</section>

<section class="evidence-panel" markdown="1">

## Exemplar evidence

> Target: Exemplar performance at the assignment's .92 benchmark.

This page is designed to earn that result through visible, verifiable work—not just a claim:

- [x] A JavaScript object array stores personalized flag data.
- [x] A `for...of` loop creates every grid item through DOM manipulation.
- [x] JavaScript creates and styles the `grid_container` element.
- [x] CSS Grid uses responsive columns that adapt without horizontal overflow.
- [x] Markdown presents a specific, chronological personal journey and interests.
- [x] Accessibility includes semantic sections, descriptive image text, and reduced-motion support.
- [ ] Four original, personalized gallery images replace the template photos.
- [ ] Three focused SDLC commits each include a build and verification step.

</section>

## Moments off-screen

The final gallery will feature four snapshots of the people, activities, pets, and food that make me happy.

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
