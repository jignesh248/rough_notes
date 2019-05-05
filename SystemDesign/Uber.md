
- SQLAlchemy
- https://github.com/google/s2geometry
- ringpop
- https://www.brianstorti.com/swim/
- https://github.com/Project-OSRM/osrm-backend
- https://github.com/twitter/twemproxy
- https://github.com/golang/geo
- https://blog.nobugware.com/post/2016/geo_db_s2_geohash_database/

https://github.com/steveyen/gtreap
https://blog.nobugware.com/post/2016/geo_db_s2_geohash_database/ //TODO indepth
https://github.com/golang/geo //TODO
https://s2geometry.io/about/overview //TODO

Big Endian //TODO
hilbert curve //TODO

https://eng.uber.com/schemaless-part-one/ //TODO
Doubt : "failing MySQL masters" didn't get it, because write capacity is reached and as such writes needs to be buffered or what?
https://eng.uber.com/schemaless-part-two/ //TODO
https://eng.uber.com/schemaless-part-three/ //TODO

doubt: understood the inconsistency with redis when writes were not available in DB, but didn't get the part which states "Redis-based solution did not scale", what other problem did they face and why(I know the one stated is in itself good enough reason to move away but still)

doubt: but favoring write availability over read-your-write semantics.
does the author mean they don't want to do read-your-write to avoid reading stale data or the author wants to imply to not care about read-your-write to favour write availability. The use of word "over" is confusing here, it can be over as something given more preference, or some


http://eng.uber.com/mezzanine-migration/ topic : DB migration //TODO