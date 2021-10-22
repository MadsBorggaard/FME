CREATE TABLE [dbo].[FME_Statestik](
	[dato] [datetime2](7) NOT NULL,
	[id] [nchar](36) NULL,
	[name] [nvarchar](max) NULL,
	[status] [nvarchar](20) NULL,
	[elapsedRunTime] [float] NULL,
	[cpuSysTime] [float] NULL,
	[cpuUserTime] [float] NULL,
	[cpuTime] [float] NULL,
	[failureMessage] [nvarchar](max) NULL,
	[featuresRead] [nvarchar](max) NULL,
	[featuresWritten] [nvarchar](max) NULL,
	[totalFeaturesRead] [bigint] NULL,
	[totalFeaturesWritten] [bigint] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
