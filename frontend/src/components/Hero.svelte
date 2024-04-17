<script>
  import Header from "../components/Header.svelte";
  import SectionWrapper from "./SectionWrapper.svelte";
  import { onMount, onDestroy } from "svelte";

  let isLoading = false;
  let buttonText = "Retrieve Data";
  let buttonTexts = [
    "Retrieving Data",
    "Retrieving Data.",
    "Retrieving Data..",
    "Retrieving Data...",
    "I'm hard at work.",
    "They only gave me 1gb of RAM to work with.",
    "Trying my best.",
    "ChatGPT taught me how to make a button do this.",
    "I haven't had my coffee yet.",
    "Really trying.",
    "I'm not a very fast reader.",
    "Sorry...",
  ];
  let index = 0;
  let intervalid;

  let sections = {
    "amazon-devices": false,
    audible: false,
    automotive: false,
    "baby-products": false,
    beauty: false,
    books: false,
    fashion: false,
    computers: false,
    electronics: false,
    garden: false,
    "gift-cards": false,
    health: false,
    home: false,
    "home-improvement": false,
    kitchen: false,
    lighting: false,
    "movies-and-tv": false,
    music: false,
    "musical-instruments": false,
    grocery: false,
    "pet-supplies": false,
    software: false,
    "sporting-goods": false,
    "office-products": false,
    toys: false,
    videogames: false,
  };

  let data = null;
  async function submitForm() {
    isLoading = true;
    buttonText = buttonTexts[0];
    index = 1;
    await new Promise((r) => setTimeout(r, 2000));
    intervalid = setInterval(() => {
      index = (index + 1) % buttonTexts.length;
      buttonText = buttonTexts[index];
    }, 4000);
    const selectedSections = Object.keys(sections).filter(
      (key) => sections[key]
    );
    console.log(selectedSections);
    const response = await fetch("http://127.0.0.1:6969/api/amazon", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ sections: selectedSections }),
    });
    data = await response.json();
    isLoading = false;
    clearInterval(intervalid);
  }

  onMount(() => {
    return () => clearInterval(intervalid);
  });
</script>

<SectionWrapper>
  <Header />
  <div class="flex flex-col gap-10 flex-1 items-center justify-center py-10">
    <h2 class="text-8xl font-semibold">Amazon Web Scraper Demo</h2>
    <div class="max-w-6xl max-auto">
      <h2 class="mb-4 text-2xl font-semibold text-center">
        Select the categories you want to scrape and receive the names, price
        and rating of the top 5 products in that category.
      </h2>
    </div>
    <div class="flex flex-col flex-auto max-w-full">
      <form
        class="grid grid-cols-3 gap-4"
        on:submit|preventDefault={submitForm}
      >
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["amazon-devices"]}
          />
          Amazon Devices
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.audible} />
          Audible
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.automotive}
          />
          Automotive
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["baby-products"]}
          />
          Baby Products
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.beauty} />
          Beauty
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.books} />
          Books
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.computers}
          />
          Computers
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.electronics}
          />
          Electronics
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.fashion} />
          Fashion
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.garden} />
          Garden
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["gift-cards"]}
          />
          Gift Cards
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.grocery} />
          Grocery
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.health} />
          Health
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.home} />
          Home
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["home-improvement"]}
          />
          Home Improvement
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.kitchen} />
          Kitchen
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.lighting}
          />
          Lighting
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["movies-and-tv"]}
          />
          Movies & TV
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.music} />
          Music
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["musical-instruments"]}
          />
          Musical Instruments
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["office-products"]}
          />
          Office Products
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["pet-supplies"]}
          />
          Pet Supplies
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.software}
          />
          Software
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections["sporting-goods"]}
          />
          Sporting Goods
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input type="checkbox" class="mr-2" bind:checked={sections.toys} />
          Toys
        </label>
        <label class="block text-lg font-medium text-gray-700">
          <input
            type="checkbox"
            class="mr-2"
            bind:checked={sections.videogames}
          />
          Video Games
        </label>
        <button
          type="submit"
          class="col-span-3 mt-4 py-2 px-4 text-white rounded transition-colors duration-300 {isLoading
            ? 'bg-gray-500 cursor-not-allowed'
            : 'bg-blue-500 hover:bg-blue-700'}"
          on:click|preventDefault={submitForm}
          disabled={isLoading}
        >
          {#if isLoading}
            <div class="spinner"></div>
            <span>{buttonText}</span>
          {:else}
            Retrieve Data
          {/if}
        </button>
      </form>
      {#if data}
        {#each Object.keys(data) as section}
          <h2 class="text-center text-2xl font-semibold py-6">{section}</h2>
          {#each data[section].product_names as name, index}
            <div
              class="grid grid-cols-2 gap-4 items-center justify-center py-6"
            >
              <div class="text-center">
                <h3 class="text-xl pb-4">{name}</h3>
                <p class="text-base pb-2">
                  Price: {data[section].product_prices[index]}
                </p>
                <p class="text-base">
                  Rating: {data[section].product_ratings[index]}
                </p>
              </div>
              <img
                class="mx-auto w-64 h-64 object-cover"
                alt="Product"
                src={data[section].product_images[index]}
              />
            </div>
          {/each}
        {/each}
      {/if}
    </div>
  </div>
</SectionWrapper>
