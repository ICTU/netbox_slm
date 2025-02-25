# Changelog

## [Unreleased]

## [1.8.0](https://github.com/ICTU/netbox_slm/releases/tag/1.8.0) - 2025-02-25

### Added

* Toggle to show plugin as top level menu item (#42)
* Bulk import and bulk edit (#4)
* Changelog with backdated changes (#51)
* List filtering (#54)
* Show installations on native objects (#49)
* SPDX license expressions (#47)

### Changed

* Support NetBox v4.2.3 (#51)
* Render objects consistently (#58)

### Fixed

* Model detail view listing of linked objects (#55)
* Search link of installations table cells (#48)

## [1.7.0](https://github.com/ICTU/netbox_slm/releases/tag/1.7.0) - 2024-07-09

### Changed

* Support NetBox v4.0.6 (#38)

### Fixed

* Hidden plugin data when not logged in (#37)

### Removed
 
* Broken bulk import and bulk edit (#4)

## [1.6.0](https://github.com/ICTU/netbox_slm/releases/tag/1.6.0) - 2024-02-13

### Added

* Additional `SoftwareProductVersion` fields (#10)
* Additional `SoftwareLicense` fields (#26)

### Changed

* Support NetBox v3.7.2 (#35)

## [1.5](https://github.com/ICTU/netbox_slm/releases/tag/1.5) - 2023-10-04

### Added

* Hyperlink option for `SoftwareLicense.stored_location` (#27)

### Changed

* Update docs and imports for newer NetBox versions (#23)
* Support NetBox v3.6.1 (#21)
* Allow linking `SoftwareProductInstallation` to `Cluster` (#17)

### Fixed

* Date picker for start and expiration dates (#22)

## [1.4](https://github.com/ICTU/netbox_slm/releases/tag/1.4) - 2023-06-30

### Added

* License information for software installations (#8)

### Changed

* Replace `NetBoxModelCSVForm` with `NetBoxModelImportForm` (#18)

## [1.3](https://github.com/ICTU/netbox_slm/releases/tag/1.3) - 2023-04-19

### Added

* Set up continuous integration (#3)

### Changed

* Support NetBox v3.4.7 (#14)

### Fixed

* Unify API serialization (#12)

## [1.2](https://github.com/ICTU/netbox_slm/releases/tag/1.2) - 2022-05-19

* Fixed filtering of relevant versions when adding a new installation
* Manufacturer is now required for the add software product form

## [1.1](https://github.com/ICTU/netbox_slm/releases/tag/1.1) - 2022-05-03

* Fixed search filter
