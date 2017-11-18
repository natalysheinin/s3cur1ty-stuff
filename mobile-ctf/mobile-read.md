## The Beginner's Guide to Mobile CTFs

### Walkthrough
* Figure out what to do with an **IPA** file - unzip it!
* Analyze all the things using Linux command `strings` - Run strings on any binary, file, etc to search for strings! `strings <file-name> | grep "flag"`
* Analyze iOS' **Assets.car** file - Run Apple's `assetutil` on the Assets.car file - `xcrun --sdk iphoneos assetutil --info Assets.car` [See StackOverflow for more](https://stackoverflow.com/questions/22630418/analysing-assets-car-file-in-ios)
* Extract stuff out of the **Assets.car** file (like images) & homebrew friendly - [Asset Catalog Tinkerer](https://github.com/insidegui/AssetCatalogTinkerer)

* Here is the CTF I participated in: [iOS CTF](https://www.ivrodriguez.com/mobile-ctf) by [Ivan](https://github.com/ivRodriguezCA)





