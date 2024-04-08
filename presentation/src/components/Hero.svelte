<script>
  import Header from "../components/Header.svelte";
  import SectionWrapper from "./SectionWrapper.svelte";
</script>

<SectionWrapper>
  <Header />
  <div class="flex flex-col gap-10 flex-1 items-center justify-center pb-10">
    <h2 class="text-8xl font-semibold">Main Point of Presentation.</h2>
    <p class="text-4xl">We also have other points besides the main point!</p>
    <p class="text-2xl">We have so many points...</p>
    <p class="text-xl">
      If you scroll down these points will be elaborated on.
    </p>
  </div>
</SectionWrapper>
