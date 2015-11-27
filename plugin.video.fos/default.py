# -*- coding: utf-8 -*-
import xbmcaddon,os,requests
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys
PLUGIN='plugin.video.fos'
ADDON = xbmcaddon.Addon(id=PLUGIN)
username = ADDON.getSetting('user')
password = ADDON.getSetting('pass')
domain = ADDON.getSetting('server')
port = ADDON.getSetting('port')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
_addon = xbmcaddon.Addon()
_path = _addon.getAddonInfo("path")
def CATEGORIES():
    addDir('[COLOR green]Welcome Team eXpat[/COLOR]','','','')
    r = requests.get('http://%s:%s/playlist.php?username=%s&password=%s&m3u'%(domain,port,username,password))
    match = re.compile('EXTINF:0,(.+?)\r.(.+?)\r',re.DOTALL).findall(r.content)
    for name,url in match:
        addDir2('[COLOR gold]%s[/COLOR]'%name,url,10,'')
    addDir('[COLOR yellow]Live Streams[/COLOR]','','','')
    url = ('http://pastebin.com/raw.php?i=2dM1k6tR')
    r = requests.get(url)
    match = re.compile('EXTINF:.+?,(.+?)\r\n(.+?)\r').findall(r.content)
    for name,url in match:
        if '———' in name:
            addDir2('[COLOR red]%s[/COLOR]'%name,url,10,'')
        else:
            addDir2(name,url,10,'')

def PLAYVIDEO(name,url):
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Featching Your Video',name)
        dp.close()
        play.play(url)
def PLAYVIDEO2(url):
    import urlresolver
    from urlresolver import common
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve()
    play.play(url)
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True
 
                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
        
elif mode==2:
        print ""+url
        addSearch()
elif mode==8:
        userpanel()
elif mode==9:
        userpanel2()

elif mode==10:
        PLAYVIDEO(name,url)
elif mode==11:
        ONDEMAND()
elif mode==12:
        PLAYVIDEO2(url)
elif mode==13:
        FULLMATCH(url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
