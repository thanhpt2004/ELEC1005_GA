<script>
  import SectionWrapper from "./SectionWrapper.svelte";
</script>

<SectionWrapper>
  <div class="flex flex-row justify-center p-4">
    <div class="flex flex-col flex-grow">
      <h3 class="text-4xl text-left pb-4">Subheading</h3>
      <p class="text-2xl text-justify pr-4">
        A sample paragraph of text that is very long. It contains a lot of words
        becuase this is a template I am making and I want there to be a complete
        paragrah here on my website. It is currently 4:45 pm and it has been a
        nice day.
      </p>
    </div>

    <div>
      <img
        src="https://expertphotography.b-cdn.net/wp-content/uploads/2019/03/yns-plt-527773-unsplash-1.jpg"
        alt="Goofy Man"
        class="flex-shrink-0"
      />
    </div>
  </div>
</SectionWrapper>
