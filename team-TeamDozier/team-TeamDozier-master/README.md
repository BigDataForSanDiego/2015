# team-TeamDozier
http://jessdozier.maps.arcgis.com/apps/MapSeries/index.html?appid=274dd578a67242b1bb496c746c5d76dc

https://jessicadozier.proto.io/share/?id=2546bd4a-92a5-44ba-9943-56d0caa284ab&v=2

Currently, SDSU does not have access to the "GeoEvent Extension" so the real-time monitoring features were not able to be fully incoprorated. A license is $5,000 and there is no free trial available for this extension. 

Connect to Real-Time Streaming Data: Incorporate real-time information streams. Connect sensors to features to represent up-to-date information as it occurs. 
    This feature is available, but I set the "Refresh Interval" for each dataset's feed to 3 minutes (following NOAA's set frequency at 2-3 minutes. This allows all of the data collected from the web services to be updated, thus allowing the closest collection of real-time data possible without using the GeoEvent extension.
    
    
Analyze and Process Real-Time Data: Filter streams of data using spatial and attribute functions to focus on the most interesting features. Modify and enrich data streams with additional attributes and descriptive information.
    Creating a "GeoFence" with this feature allows for alerts to be sent once specific data is detected within the GeoFence. This will be applied to the 3 mile buffer zones around each of the contacts, so when a disaster (updated every 3 minutes directly from NWS, NOAA, IGEMS, ArcGIS Live Feeds, and San Diego County) occurs within a buffer zone, the user will instantly be notified via the app's Push Notification, text message, and email. Directions to apply this can be found here: http://server.arcgis.com/en/geoevent-extension/latest/process-event-data/overview-of-output-connectors.htm
    

Bringing your applications to life: Streaming data from the GeoEvent Extension can be utilized by the entire ArcGIS system to bring everyday GIS applications to life. The GeoEvent Extension enables the integration of streaming data into an enterprise GIS by updating feature services and other online content. The features and content can then be consumed in web maps and viewers such as the Operations Dashboard for ArcGIS (or any ArcGIS viewer) to display the most up-to-date information on events as they unfold. 
    This will allow each contacts' locations to be monitored
    
    
This app is a hybrid app which is available on different platforms (browser, mobile, tablets). There is also an availability for the Operations Dashboard to be downloaded for any formal institution use (such as San Diego County OES, Red Cross, etc).
