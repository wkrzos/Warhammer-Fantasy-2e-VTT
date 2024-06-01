import os
from backend.character_sheets.sheets import Card, Character, CharacterDescription, Statistics, Races
from backend.json_serialisation.save_manager import SaveManager

def create_sample_card():
    # Create a sample character description
    character_description = CharacterDescription(
        colorOfEyes="Blue",
        colorOfHairs="Blonde",
        weight=75,
        height=180,
        sex="Male",
        age=30,
        starSign="The Twins",
        birthplace="Altdorf",
        distenguishingMarks="Scar on left cheek",
        previousProfession="Mercenary",
        currentProfession="Knight"
    )

    # Create sample statistics
    statistics = Statistics(
        ws=50,
        bs=45,
        s=40,
        t=35,
        ag=30,
        int=25,
        wp=20,
        fel=15,
        w=10,
        m=4,
        magic=2,
        ip=0,
        fp=1
    )

    # Create a sample character
    character = Character(
        name="Sample Character",
        race=Races("r.1"),
        statistics=statistics
    )

    # Create a sample card
    card = Card(
        playerName="Sample Player",
        playerCharacter=character,
        characterPicture="path/to/sample/image.png",
        characterDescription=character_description,
        history="This is the history of the sample character."
    )

    return card

def test_save_character_card():
    card = create_sample_card()
    save_path = os.path.normpath("saves/cards")
    save_name = "test_character"

    # Save the character card
    SaveManager.saveCharacterCard(characterCard=card, localisation=save_path, saveName=save_name)

    # Check if the file was created
    file_path = os.path.join(save_path, save_name + ".json")
    file_path = os.path.normpath(file_path)

    if os.path.exists(file_path):
        print(f"Test passed! File saved at: {file_path}")
    else:
        print("Test failed! File not found.")

if __name__ == "__main__":
    test_save_character_card()
