using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using WebSocketSharp;

namespace demo_wss
{


    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    [Serializable]
    public struct CompactMarketData
    {
        public byte Exchange;
        public Int32 InstrumentToken;
        public Int32 LastTradedPrice;
        public Int32 Change;
        public Int32 ExchangeTimeStamp;
        public Int32 Volume;
        
    }

    public class CompactMarketTick
    {
        public byte Exchange;
        public Int32 InstrumentToken;
        public Int32 LastTradedPrice;
        public Int32 Change;
        public Int32 ExchangeTimeStamp;
    }


    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    [Serializable]
    public struct MarketData
    {
        public byte Exchange;
        public Int32 InstrumentToken;
        public Int32 LastTradedPrice;
        public Int32 LastTradeTime;
        public Int32 LastTradeQty;
        public Int32 Volume;
        public Int32 BestBidPrice;
        public Int32 BestBidQty;
        public Int32 BestAskPrice;
        public Int32 BestAskQty;
        public Int64 TotalBuyQty;
        public Int64 TotalSellQty;
        public Int32 AverageTradePrice;
        public Int32 ExchangeTimeStamp;
        public Int32 OpenPrice;
        public Int32 HighPrice;
        public Int32 LowPrice;
        public Int32 ClosePrice;
        public Int32 YearlyHigh;
        public Int32 YearlyLow;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    [Serializable]
    public struct OpenInterest
    {
        public byte Exchange;
        public Int32 InstrumentToken;
        public Int32 CurrentOpenInterest;
        public Int32 InitialOpenInterest;
        public Int32 ExchangeTimeStamp;
    }




    public class FullMarketTick
    {
        public byte Exchange;
        public Int32 InstrumentToken;
        public Int32 LastTradedPrice;
        public Int32 LastTradeTime;
        public Int32 LastTradeQty;
        public Int32 Volume;
        public Int32 BestBidPrice;
        public Int32 BestBidQty;
        public Int32 BestAskPrice;
        public Int32 BestAskQty;
        public Int64 TotalBuyQty;
        public Int64 TotalSellQty;
        public Int32 AverageTradePrice;
        public Int32 ExchangeTimeStamp;
        public Int32 OpenPrice;
        public Int32 HighPrice;
        public Int32 LowPrice;
        public Int32 ClosePrice;
        public Int32 YearlyHigh;
        public Int32 YearlyLow;
        public Int32 HighCircuitLimit;
        public Int32 LowCircuitLimit;
        public Int32 CurrentOpenInterest;
        public Int32 InitialOpenInterest;
    }
    



    class Program
    {

        static WebSocket ws;
        static int exchange1, exchange2,exchange3, intrumenttoken1, intrumenttoken2, intrumenttoken3;
        static void Main(string[] args)
        {
            Console.WriteLine("Enter Access token(Copy and paste access token from oauth response):");
            var accesskey = Console.ReadLine();  ///Copy and paste access token from oauth response after login success

            ws = new WebSocket("wss://masterswift-beta.mastertrust.co.in/hydrasocket/v2/websocket?acess_token=" + accesskey);

            ws.OnClose += Ws_OnClose;
            ws.OnMessage += Ws_OnMessage;
            ws.OnError += Ws_OnError;

            ws.Connect();
            var subscriptionList = new List<string>();
            //NSE=1,NFO=2,CDS=3,MCX=4,BSE=6

            //exchange1 = 2; //NSE
            //intrumenttoken1 = 44461; //ACC-EQ

            //exchange2 = 1;  //NSE
            //intrumenttoken2 = 1330;//HDFC-EQ

            exchange3 = 4;  //MCX
            intrumenttoken3 = 215546; //CRUDEOIL20JANFUT

            subscriptionList.Add(" [" + exchange3 + ", " + intrumenttoken3 + " ]");
            // subscriptionList.Add(" [" + exchange2 + ", " + intrumenttoken2 + " ]");
            // subscriptionList.Add(" [" + exchange3 + ", " + intrumenttoken3 + " ]");
            var subscriptionItem = string.Join(", ", subscriptionList);

            var msg = "{\"a\": \"subscribe\",\"v\":[" + subscriptionItem + "], \"m\": \"compact_marketdata\"}";
            ws.Send(msg);

            Console.WriteLine("Press Enter to stop");
            do
            {
                while (!Console.KeyAvailable)
                {
                    
                }
            } while (Console.ReadKey(true).Key != ConsoleKey.Enter);
            var msg1 = "{\"a\": \"unsubscribe\",\"v\":[" + subscriptionItem + "], \"m\": \"compact_marketdata\"}";
            ws.Send(msg1);
        }

        private static void Ws_OnError(object sender, ErrorEventArgs e)
        {
            Console.WriteLine("Socket error "+e );
        }

        private static void Ws_OnMessage(object sender, MessageEventArgs e)
        {
            if (e.IsBinary)
            {
                var data = e.RawData;
                var offset = 0;
                var mode = data[offset];
                offset++;
                switch (mode)
                {
                    //market data
                    //case 1:
                    //    ReadMarketData(data, ref offset);
                    //break;
                    //case 3:
                    //    //ReadSnapQuote(data, ref offset);
                    //    //break;
                    case 2:
                        ReadCompactMarketData(data, ref offset);
                        break;
                    //case 8:
                    //    ReadOpenIntrest(data, offset);
                    //    break;
                }
            }
        }

        private static void Ws_OnClose(object sender, CloseEventArgs e)
        {
            Console.WriteLine("Socket closed");
        }

        private static void ReadCompactMarketData(byte[] data, ref int offset)
        {
            var length = data.Length - offset;
            IntPtr dataPacket = Marshal.AllocHGlobal(length);
            Marshal.Copy(data, offset, dataPacket, length);
            var marketData = (CompactMarketData)Marshal.PtrToStructure(dataPacket, typeof(CompactMarketData));
            Marshal.FreeHGlobal(dataPacket);
            var val = Formatchange(marketData);
            decimal divisor = 100;
            if (val.Exchange == 3) divisor = 10000000;
            decimal out1= val.LastTradedPrice / divisor;
            Console.WriteLine("LTP is:" + out1);
        }
        private static void ReadOpenIntrest(byte[] data, int offset)
        {
            var length = data.Length - offset;
            IntPtr dataPacket = Marshal.AllocHGlobal(length);
            Marshal.Copy(data, offset, dataPacket, length);
            var oiData = (OpenInterest)Marshal.PtrToStructure(dataPacket, typeof(OpenInterest));
            Marshal.FreeHGlobal(dataPacket);
             Formatchange(oiData);
            
        }

        //private static void ReadSnapQuote(byte[] data, ref int offset)
        //{
        //    var length = data.Length - offset;
        //    IntPtr snapPacket = Marshal.AllocHGlobal(length);
        //    Marshal.Copy(data, offset, snapPacket, length);
        //    var snapData = (SnapQuote)Marshal.PtrToStructure(snapPacket, typeof(SnapQuote));
        //    Marshal.FreeHGlobal(snapPacket);
        //   // var val = Formatchange(snapData);
        //    //OnSnapQuoteUpdateEvent(val);
        //}

        private static CompactMarketData Formatchange(CompactMarketData data)
        {
            var marketdata = new CompactMarketData();
            marketdata.Exchange = data.Exchange;
            marketdata.InstrumentToken = Formatchange(data.InstrumentToken);
            marketdata.LastTradedPrice = Formatchange(data.LastTradedPrice);
            marketdata.Volume = Formatchange(data.Volume);
            marketdata.Change = Formatchange(data.Change);
            return marketdata;
        }

        private static FullMarketTick Formatchange(OpenInterest data)
        {
            var marketData = new FullMarketTick();
            //marketData.Type = MarketDataType.OI;
            marketData.Exchange = data.Exchange;
            marketData.InstrumentToken = Formatchange(data.InstrumentToken);
            marketData.ExchangeTimeStamp = Formatchange(data.ExchangeTimeStamp);
            marketData.CurrentOpenInterest = Formatchange(data.CurrentOpenInterest);
            marketData.InitialOpenInterest = Formatchange(data.InitialOpenInterest);
            Console.WriteLine("Current OI is:" + marketData.CurrentOpenInterest + "  ,Initial OI:"+ marketData.InitialOpenInterest);
            return marketData;
        }

        //private static void ReadMarketData(byte[] data, ref int offset)
        //{
        //    var length = data.Length - offset;
        //    IntPtr dataPacket = Marshal.AllocHGlobal(length);
        //    Marshal.Copy(data, offset, dataPacket, length);
        //    var marketData = (MarketData)Marshal.PtrToStructure(dataPacket, typeof(MarketData));
        //    Marshal.FreeHGlobal(dataPacket);
        //    var val = Formatchange(marketData);
        //    Console.WriteLine("LTP is:" + val.LastTradedPrice / 100);
        //}

        //private static FullMarketTick Formatchange(MarketData data)
        //{
        //    var marketdata = new FullMarketTick();
        //    marketdata.Exchange = data.Exchange;
        //    marketdata.InstrumentToken = Formatchange(data.InstrumentToken);
        //    marketdata.AverageTradePrice = Formatchange(data.AverageTradePrice);
        //    marketdata.BestAskQty = Formatchange(data.BestAskQty);
        //    marketdata.BestBidPrice = Formatchange(data.BestBidPrice);
        //    marketdata.BestBidQty = Formatchange(data.BestBidQty);
        //    marketdata.BestAskPrice = Formatchange(data.BestAskPrice);
        //    marketdata.ExchangeTimeStamp = Formatchange(data.ExchangeTimeStamp);
        //    marketdata.ClosePrice = Formatchange(data.ClosePrice);
        //    marketdata.HighPrice = Formatchange(data.HighPrice);
        //    marketdata.OpenPrice = Formatchange(data.OpenPrice);
        //    marketdata.Volume = Formatchange(data.Volume);
        //    marketdata.LowPrice = Formatchange(data.LowPrice);
        //    marketdata.YearlyHigh = Formatchange(data.YearlyHigh);
        //    marketdata.YearlyLow = Formatchange(data.YearlyLow);
        //    marketdata.LastTradeQty = Formatchange(data.LastTradeQty);
        //    marketdata.LastTradeTime = Formatchange(data.LastTradeTime);
        //    marketdata.LastTradedPrice = Formatchange(data.LastTradedPrice);
        //    marketdata.TotalBuyQty = Formatchange(data.TotalBuyQty);
        //    marketdata.TotalSellQty = Formatchange(data.TotalSellQty);
        //    return marketdata;
        //}

        private static int Formatchange(int intVal)
        {
            var temp = BitConverter.GetBytes(intVal);
            if (BitConverter.IsLittleEndian) Array.Reverse(temp);
            intVal = BitConverter.ToInt32(temp, 0);
            return intVal;
        }

        private static long Formatchange(long longVal)
        {
            var temp = BitConverter.GetBytes(longVal);
            if (BitConverter.IsLittleEndian) Array.Reverse(temp);
            longVal = BitConverter.ToInt64(temp, 0);
            return longVal;
        }
    }
}