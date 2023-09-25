var getid=async function(sec_user_id,max_cursor){
	var res=await fetch("https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id="+sec_user_id+"&max_cursor="+max_cursor, {
	  "headers": {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi",
		"sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin"
	  },
	  "referrer": "https://www.douyin.com/user/MS4wLjABAAAA5A-hCBCTdv102baOvaoZqg7nCIW_Bn_YBA0Aiz9uYPY",
	  "referrerPolicy": "strict-origin-when-cross-origin",
	  "body": null,
	  "method": "GET",
	  "mode": "cors",
	  "credentials": "include"
	});
	try{
	    res=await res.json();
	}catch(e){
		res=await getid(sec_user_id,max_cursor);
		console.log(e);
	}
	return res;
}

// 得到下载地址，类似下面的
// "http://v3-web.douyinvod.com/23ac534f948453106e50a3f89126ed5f/650c0504/video/tos/cn/tos-cn-ve-15c001-alinc2/oAUdqBgyGhoPyDJyA2QXEwILNrAA6BAD3zEehf/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=3959&bt=3959&cs=0&ds=4&ft=X1nbLXvvBQ3AUq8yq8Z..NnGSYKeIALDtGXQLCPAq8_4&mime_type=video_mp4&qs=0&rc=NzYzNDg2M2c5ZjZnZ2hpZUBpM3FyNTc6ZmR1bjMzNGkzM0BiMTAwLWEyXmAxLmNiLjAuYSNvMDVtcjQwXzJgLS1kLTBzcw%3D%3D&btag=e00008000&dy_q=1695282925&l=202309211555259261EAA62AAAA3067B05",
// "http://v26-web.douyinvod.com/fd0ac82844ed43874c747b7452d847f7/650c0504/video/tos/cn/tos-cn-ve-15c001-alinc2/oAUdqBgyGhoPyDJyA2QXEwILNrAA6BAD3zEehf/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=3959&bt=3959&cs=0&ds=4&ft=X1nbLXvvBQ3AUq8yq8Z..NnGSYKeIALDtGXQLCPAq8_4&mime_type=video_mp4&qs=0&rc=NzYzNDg2M2c5ZjZnZ2hpZUBpM3FyNTc6ZmR1bjMzNGkzM0BiMTAwLWEyXmAxLmNiLjAuYSNvMDVtcjQwXzJgLS1kLTBzcw%3D%3D&btag=e00008000&dy_q=1695282925&l=202309211555259261EAA62AAAA3067B05",
// "https://www.douyin.com/aweme/v1/play/?video_id=v0300fg10000ck5rba3c77u4p28o3nr0&line=0&file_id=1b3f1eedfd134cc6ad50d305313043e4&sign=f2034391af62f02877dcb465b557031a&is_play_url=1&source=PackSourceEnum_PUBLISH"
var download=async function(url, aweme_id, desc){
	var file_name = aweme_id + "-" + desc + ".mp4";
	var data=await fetch(url, {
  "headers": {
    "accept": "*/*",
    "accept-language": "vi,en-US;q=0.9,en;q=0.8",
    "range": "bytes=0-",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "video",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
  },
  "referrer": "https://www.douyin.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
});
	data=await data.blob();
	var a = document.createElement("a");
	a.href = window.URL.createObjectURL(data);
	a.download = file_name;
	a.click();
}

var waitforme=function(millisec) {
    return new Promise(resolve => {
        setTimeout(() => { resolve('') }, millisec);
    })
}

var run=async function(){
	var result=[];
	var hasMore=1;
	var sec_user_id=location.pathname.replace("/user/","");
	var max_cursor=0;
	var download_from=prompt("Enter id video(Enter 0 if want to download all video):","");
	if(download_from==null || download_from=="") {
		alert("Please, Enter id of video!");
		return;
	}
	while(hasMore==1){
		var moredata=await getid(sec_user_id,max_cursor);
		hasMore=moredata['has_more'];
		max_cursor=moredata['max_cursor'];
		for(var i in moredata['aweme_list']){
			if(moredata['aweme_list'][i]['aweme_id'] == download_from){
				hasMore=0;
				break;
			}
			if(moredata['aweme_list'][i]['video']['play_addr']['url_list'][0].startsWith("https"))
				result.push([moredata['aweme_list'][i]['video']['play_addr']['url_list'][0],moredata['aweme_list'][i]['aweme_id'],moredata['aweme_list'][i]['desc']]);
			else
				result.push([moredata['aweme_list'][i]['video']['play_addr']['url_list'][0].replace("http","https"),moredata['aweme_list'][i]['aweme_id'],moredata['aweme_list'][i]['desc']]);
			
			console.clear();
			console.log("Number of videos: "+result.length);
			if(result.length>10){
				hasMore=0;
				break;
			}
		}
	}
	for(var i=result.length-1;i>=0;i--){
		await waitforme(1000);
		try{download(result[i][0],result[i][1],result[i][2]);}catch{}
	}
}

run();