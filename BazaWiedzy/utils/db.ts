import { PrismaClient } from "@prisma/client";

const globalForPrisma = global as unknown as {
  prisma: PrismaClient | undefined;
};

function getPrisma() {
  if (globalForPrisma.prisma) return globalForPrisma.prisma;
  else {
    globalForPrisma.prisma = new PrismaClient({
      log: ["query"],
    });

    // Makes sure that new articles are not public by default
    globalForPrisma.prisma.$use(async (params, next) => {
      if (params.model == "Article" && params.action == "create") {
        params.args.data.public = false;
      }
      return await next(params);
    });

    return globalForPrisma.prisma;
  }
}

export const prisma = getPrisma();
