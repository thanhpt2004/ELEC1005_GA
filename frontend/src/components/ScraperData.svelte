<script>
  import SectionWrapper from "./SectionWrapper.svelte";

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
  }
</script>

<SectionWrapper>
  <h1 class="mb-4 text-4xl font-bold">Web Scraper Demo</h1>
  <h2 class="mb-4 text-2xl font-semibold">
    Select the sections you want to scrape and receive the names, price and
    rating of the top 5 products in that category.
  </h2>
  <div class="flex flex-col flex-1">
    <form class="flex flex-col" on:submit|preventDefault={submitForm}>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["amazon-devices"]}
        />
        Amazon Devices
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.audible} />
        Audible
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections.automotive}
        />
        Automotive
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["baby-products"]}
        />
        Baby Products
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.beauty} />
        Beauty
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.books} />
        Books
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.fashion} />
        Fashion
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.computers} />
        Computers
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections.electronics}
        />
        Electronics
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.garden} />
        Garden
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["gift-cards"]}
        />
        Gift Cards
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.health} />
        Health
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.home} />
        Home
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["home-improvement"]}
        />
        Home Improvement
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.kitchen} />
        Kitchen
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.lighting} />
        Lighting
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["movies-and-tv"]}
        />
        Movies & TV
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.music} />
        Music
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["musical-instruments"]}
        />
        Musical Instruments
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.grocery} />
        Grocery
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["pet-supplies"]}
        />
        Pet Supplies
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.software} />
        Software
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["sporting-goods"]}
        />
        Sporting Goods
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections["office-products"]}
        />
        Office Products
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input type="checkbox" class="mr-2" bind:checked={sections.toys} />
        Toys
      </label>
      <label class="block text-sm font-medium text-gray-700">
        <input
          type="checkbox"
          class="mr-2"
          bind:checked={sections.videogames}
        />
        Video Games
      </label>
      <button
        type="submit"
        class="mt-4 py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-700 transition-colors duration-300"
        >Retrieve Data</button
      >
    </form>
    {#if data}
      {#each Object.keys(data) as section}
        <h2 class="text-2xl font-semibold">{section}</h2>
        {#each data[section].product_names as name, index}
          <div>
            <h3 class="text-xl">{name}</h3>
            <p>Price: {data[section].product_prices[index]}</p>
            <p>Rating: {data[section].product_ratings[index]}</p>
            <p>Image: {data[section].product_images[index]}</p>
          </div>
        {/each}
      {/each}
    {/if}
  </div>
</SectionWrapper>
