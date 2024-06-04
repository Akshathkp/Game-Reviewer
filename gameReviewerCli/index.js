const xlsx = require('xlsx');
const readline = require("readline");

try {
  // Read data from the Excel file
  const workbook = xlsx.readFile('games.xlsx');
  const sheetName = workbook.SheetNames[0];
  const sheet = workbook.Sheets[sheetName];
  const rawGames = xlsx.utils.sheet_to_json(sheet, { defval: '' });

  // Debug: Print the raw games array to check its structure
  console.log('Raw games data:', rawGames);

  // Normalize the games data to ensure correct format
  const normalizedGames = rawGames.map(game => ({
    name: game.name ? game.name.toString().trim() : '',
    genre: game.genre ? game.genre.toString().trim().toLowerCase() : '', // Convert genre to lowercase
    rating: game.rating ? parseFloat(game.rating) : 0,
  }));

  // Debug: Print the normalized games array
  console.log('Normalized games data:', normalizedGames);

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const searchGames = (searchTerm) => {
    const lowerCaseSearchTerm = searchTerm.toLowerCase();

    const results = normalizedGames.filter(game => {
      const hasValidName = game.name && typeof game.name === 'string' && game.name.trim() !== '';
      const hasValidGenre = game.genre && typeof game.genre === 'string' && game.genre.trim() !== '';

      // Debug: Print game properties being checked
      console.log('Checking game:', game);

      return (hasValidName && game.name.toLowerCase().includes(lowerCaseSearchTerm)) ||
             (hasValidGenre && game.genre.includes(lowerCaseSearchTerm)); // No need to convert genre again
    });

    if (results.length === 0) {
      console.log('No games found matching your search.');
    } else {
      console.log('Games found:');
      results.forEach(game => {
        console.log(`${game.name} (${game.genre}) - Rating: ${game.rating}`);
      });
    }
  };

  const searchGamesWithReadline = () => {
    rl.question('Enter a game name or genre: ', (searchTerm) => {
      searchGames(searchTerm.trim());
      rl.close();
    });
  };

  searchGamesWithReadline();
} catch (error) {
  console.error('Error reading or processing the Excel file:', error);
}