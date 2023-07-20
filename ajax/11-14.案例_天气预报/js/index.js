/**
 * 目标1：默认显示-北京市天气
 *  1.1 获取北京市天气数据
 *  1.2 数据展示到页面
 */
function getWeatherData(cityCode) {
    axios({
        url: 'http://hmajax.itheima.net/api/weather',
        params: {
            city: cityCode
        }
    }).then(
        res => {
            console.log(res)
            //显示公历与农历
            document.querySelector('.title').innerHTML = `
             <span class="dateShort">${res.data.data.date}</span>
        <span class="calendar">农历&nbsp;
          <span class="dateLunar">${res.data.data.dateLunar}</span>
        </span>
            `;
            //显示城市名
            document.querySelector('.area').innerText = `${res.data.data.area}`;
            //显示气温和其他天气概况
            document.querySelector('.weather-box').innerHTML = `
               <div class="tem-box">
        <span class="temp">
          <span class="temperature">${res.data.data.temperature}</span>
          <span>°</span>
        </span>
      </div>
      <div class="climate-box">
        <div class="air">
          <span class="psPm25">${res.data.data.psPm25}</span>
          <span class="psPm25Level">${res.data.data.psPm25Level}</span>
        </div>
        <ul class="weather-list">
          <li>
            <img src="${res.data.data.weatherImg}"  class="weatherImg" alt="">
            <span class="weather">${res.data.data.weather}</span>
          </li>
          <li class="windDirection">${res.data.data.windDirection}</li>
          <li class="windPower">${res.data.data.windPower}</li>
        </ul>
      </div>
            `
            //显示今天的天气情况
            document.querySelector('.today-weather').innerHTML =
                `<div class="range-box">
        <span>今天：</span>
        <span class="range">
          <span class="weather">${res.data.data.weather}</span>
          <span class="temNight">${res.data.data.todayWeather.temNight}</span>
          <span>-</span>
          <span class="temDay">${res.data.data.todayWeather.temDay}</span>
          <span>℃</span>
        </span>
      </div>
      <ul class="sun-list">
        <li>
          <span>紫外线</span>
          <span class="ultraviolet">${res.data.data.todayWeather.ultraviolet}</span>
        </li>
        <li>
          <span>湿度</span>
          <span class="humidity">${res.data.data.todayWeather.humidity}</span>%
        </li>
        <li>
          <span>日出</span>
          <span class="sunriseTime">${res.data.data.todayWeather.sunriseTime}</span>
        </li>
        <li>
          <span>日落</span>
          <span class="sunsetTime">${res.data.data.todayWeather.sunsetTime}</span>
        </li>
      </ul>
            `;
            //一周内天气情况
            //获取所有的item元素
            let weekWeather = document.querySelectorAll('.week-wrap .item');
            res.data.data.dayForecast.map((el, index) => {
                //解构赋值
                //date, dateFormat,temDay,  temNight,weather,weatherImg,windDirection, windPower
                // let { date, dateFormat, temDay, temNight, weather, weatherImg, windDirection, windPower } = el;
                let keys = Object.keys(el);
                //通过inde索引遍历赋值
                keys.forEach(key => {
                    if (key === 'weatherImg') {
                        weekWeather[index].querySelector(` .${key}`).src = el[key];
                    }
                    weekWeather[index].querySelector(` .${key}`).innerHTML = el[key];
                })
            })

        }).catch(error => console.log(error))
}
//2搜索城市列表
document.querySelector('.search-city').addEventListener('input', e => {
    console.log(e.target.value);
    axios({
        url: 'http://hmajax.itheima.net/api/weather/city',
        params: {
            city: e.target.value
        }
    }).then(res => {
        let cityList = res.data.data.map(el => {
            return `<li class="city-item" data-code = "${el.code}">${el.name}</li>`;
        }).join('');
        console.log(cityList);
        document.querySelector('.search-list').innerHTML = cityList;
    }).catch(error => console.log(error))
})
//实现切换目标城市的功能
document.querySelector('.search-list').addEventListener('click', e => {
    if (e.target.classList.contains('city-item')) {
        let cityCode = e.target.dataset.code;
        //todo:切换城市天气数据
        getWeatherData(cityCode);
    }
})
getWeatherData('110100')