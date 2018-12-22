<template>
  <div id="about">
    <h4> About Poly Professors </h4>
    <div class="section">
        <h2>Hello, and welcome to Poly Professors.</h2>
        <p>Although at the time of writing this nobody has asked me a single question about this
        website, here's what I anticipate will be some frequently asked questions:</p>

        <h2>Isn't this just a direct rip-off of polyratings?</h2>
        <p>Yep. In fact, all evaluations from polyratings have been migrated here.</p>

        <h2>Why not just use polyratings?</h2>
        <p>
            Polyratings is no longer updated, meaning no new professors can be added.
        The point of Poly Professors is to fill this void. On top of this, Poly Professors aims
        to add some more useful features as well as be all around more responsive than Polyratings.
        </p>

        <h2>Are there any big differences between this site and polyratings?</h2>
        <p>
                Besides general UI/UX changes, not much. Because all data was initially scraped from
            polyratings, I'm sort of at the mercy of their design. This also means that most of your
            design questions can be answered by viewing the FAQ at polyratings itself.
        </p>
        <p>
                A couple changes have been made, however. Poly Professors does not keep track of
        "Recognizes Student Difficulties" nor "Presents Material Clearly" like
        polyratings did. We just have one overall rating. This was an intentional design
        decision made by me, mostly because I've never once cared about those ratings, I only care
        about the total rating. Also, after evaulating these ratings it became clear that they are
        almost always the same or very similar to one another. They also seem like rather
        arbitraily chosen rating factors. However, if this feature is heavily requested it
        may be added back.
        </p>
        <h2>How was this site created?</h2>
        <p>
            Poly Professors is open source, so rather than have me explain how this site was
            created, you can simply view the actual source code linked above.
        </p>
        <h2>How can I request a feature?</h2>
        <p>To request a feature please use the contact button above.</p>
    </div>
</div>
</template>

<script>

</script>

<style scoped>

h4 {
    font-size: 36px;
}

h2 {
    font-size: 26px;
}

p {
    margin: 0;
    margin-bottom: 20px;
}

.section {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);

    margin-bottom: 100px;
    width: 1100px;
    padding: 12px 14px;

    text-align: left;
    background: white;
    border-radius: 4px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    font-size: 22px;
    border-top: 4px #2c3e50 solid;
}

</style>
