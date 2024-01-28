migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1v6d2tdwyh005gp")

  collection.name = "scraper_delay"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1v6d2tdwyh005gp")

  collection.name = "scraping_schedule"

  return dao.saveCollection(collection)
})
